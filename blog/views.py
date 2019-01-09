from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post, Facebook, Google, About, Contact, Newsletter, Email, Message
from .forms import PostForm, AboutForm, ContactForm, NewsletterForm, SendNewsletterForm
from django.db import models
from ckeditor.fields import RichTextField
from .common import getGoogleScript, getFacebookScript
import random
import string
from django.core.mail import send_mail
from django.core.mail.backends.smtp import EmailBackend
from .email_config import activation_title, activation_text, unsubscribe_text
from django.views.static import serve
import os 

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date','-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    facebooks = Facebook.objects.values_list('appId', flat=True)
    facebook = str(facebooks[0] ) if len(facebooks)>0 else None 
    facebookScript = getFacebookScript(facebook)
    return render(request, 'blog/post_detail.html', {'post': post, 'facebook' : True if facebook is not None else False, 'facebookScript' : facebookScript})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid()  and request.user.is_authenticated:
            data = form.cleaned_data
            post = Post(text=data['text'],title=data['title'],
            facebook=data['facebook'],twitter=data['twitter'],
            published_date=data['published_date'], comments=data['comments'])
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid()  and request.user.is_authenticated:
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def about(request):
    abouts = About.objects.values_list('about', flat=True)
    about = str(abouts[0] ) if len(abouts)>0 else "" 
    return render(request, 'blog/about.html', {'about': about})



def about_edit(request):
    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            data = form.cleaned_data
            about = About(about=data['about'])
            about.save()
            return redirect('about')
    else:
        form = AboutForm(instance=About.objects.get(pk=1))
    return render(request, 'blog/about_edit.html', {'form': form})



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            contact = Contact(name=data['name'],email=data['email'],text=data['text'])
            contact.add()
            return redirect('post_list')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})


def newsletter_add(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid() and len( Email.objects.values_list('smtp', flat=True))>0:
            data = form.cleaned_data
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=40))
            url = request.build_absolute_uri('?')[:-len('newsletter-add')]+"newsletter-confirm/"+code
            email = data['email']
            config = instance=Email.objects.get(pk=1)
            Newsletter.objects.filter(email=email).delete()
            newsletter = Newsletter(email=email,code=code)
            newsletter.add()
            send_mail( 
            subject=activation_title,
            message=activation_text.replace("{@url}",url),
            from_email=config.email,
            recipient_list=[email],
            auth_user=config.email,
            auth_password=config.password,
            connection=EmailBackend(
                host=config.smtp,
                port=config.sslPort,
                username=config.email,
                password=config.password,
                use_tls=False,
                use_ssl=True
            )
              )
            return redirect('post_list')
    else:
        form = NewsletterForm()
    return render(request, 'blog/newsletter_add.html', {'form': form})



def newsletter_remove(request,code):
    if code is not None:
        Newsletter.objects.filter(code=code).delete()
    return render(request, 'blog/newsletter_remove.html')


def newsletter_confirm(request,code):
    if code is not None:
        Newsletter.objects.filter(code=code).update(confirmed=True)
    url = request.build_absolute_uri('?')[:-len(code)-len('newsletter-confirm/')]+"newsletter-remove/"+code
    return render(request, 'blog/newsletter_confirm.html',{'unsubscribe':url})


def newsletter_send(request):
    if request.method == "POST":
        form = SendNewsletterForm(request.POST)
        if form.is_valid() and request.user.is_authenticated and len( Email.objects.values_list('smtp', flat=True))>0:
            data = form.cleaned_data
            text = data['text']
            title = data['title']
            message = Message(text=text,title=title)
            message.save()
            config = instance=Email.objects.get(pk=1)
            recipients = Newsletter.objects.filter(confirmed=True)
            for recipient in recipients:
                url = request.build_absolute_uri('?')[:-len('newsletter-send')]+"newsletter-remove/"+recipient.code
                send_mail( 
                subject=title,
                message="Aby odczytać wiadomość włącz obsługę html.",
                html_message=text+" " +unsubscribe_text.replace("{@url}",url),
                from_email=config.email,
                recipient_list=[recipient.email],
                auth_user=config.email,
                auth_password=config.password,
                connection=EmailBackend(
                    host=config.smtp,
                    port=config.sslPort,
                    username=config.email,
                    password=config.password,
                    use_tls=False,
                    use_ssl=True
                )
            )
            return redirect('post_list')
    else:
        form = SendNewsletterForm()
    return render(request, 'blog/newsletter_send.html', {'form': form})


def media(request,year,month,day,name):
    filepath = './media/uploads/'+year+'/'+month+'/'+day+'/'+name
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

def help(request):
    return render(request, 'blog/help.html')
