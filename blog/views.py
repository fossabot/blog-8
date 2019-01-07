from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post, Facebook
from .forms import PostForm
from django.db import models
from ckeditor.fields import RichTextField


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    facebooks = Facebook.objects.values_list('appId', flat=True)
    facebook = str(facebooks[0] ) if len(facebooks)>0 else None 
    facebookScript = """
        <div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = 'https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.2&appId={@facebookId}&autoLogAppEvents=1';
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
    """.replace("{@facebookId}",facebook)

    return render(request, 'blog/post_detail.html', {'post': post, 'facebook' : True if facebook is not None else False, 'facebookScript' : facebookScript})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post = Post(text=data['text'],title=data['title'],
            facebook=data['facebook'],twitter=data['twitter'],
            published_date=data['published_date'])
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
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
