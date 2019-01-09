from __future__ import absolute_import

from django import forms
from .models import Post, About, Contact, Email, Message
from django.forms import ModelForm, PasswordInput

from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from bootstrap_datepicker_plus import DatePickerInput
from datetime import datetime

from django.utils.translation import activate

activate('pl')

class PostForm(ModelForm):
    title = forms.CharField(label='Tytuł postu:', max_length=200, widget=forms.TextInput(),required=True)
    published_date = forms.DateField(input_formats=['%d/%m/%Y'], label='Data publikacji:',  widget=DatePickerInput(format='%d/%m/%Y'),required=True)
    text = forms.CharField(widget=CKEditorUploadingWidget(), label="",required=True)
    facebook = forms.BooleanField(label='Udostępnij przez Facebooka:', required=False)
    twitter = forms.BooleanField(label='Udostępnij przez Twittera:', required=False)
    comments = forms.BooleanField(label='Włącz komentarze:', required=False)
 
    class Meta:
        model = Post
        fields = ['title', 'published_date', 'text', 'facebook', 'twitter', 'comments']


class AboutForm(ModelForm):
    about = forms.CharField(widget=CKEditorUploadingWidget(), label="")
 
    class Meta:
        model = About
        fields = ['about']


class NewsletterForm(ModelForm):
    email = forms.CharField(label='Email', max_length=200, widget=forms.EmailInput(),min_length=7,required=True)
    class Meta:
        model = Contact
        fields = ['email']


class ContactForm(ModelForm):
    name = forms.CharField(label='Imię i nazwisko', max_length=200, widget=forms.TextInput(),min_length=7,required=True)
    email = forms.CharField(label='Email', max_length=200, widget=forms.EmailInput(),min_length=7,required=True)
    text = forms.CharField(label='Wiadomość', max_length=2000, widget=forms.Textarea,min_length=20,required=True)
 
    class Meta:
        model = Contact
        fields = ['name','email','text']



class SendNewsletterForm(ModelForm):
    title = forms.CharField(label='Temat', max_length=200)
    text = forms.CharField(widget=CKEditorUploadingWidget(), label="")
 
    class Meta:
        model = Message
        fields = ['title','text']


class EmailForm(ModelForm):
    smtp = forms.CharField(max_length=200, label="Serwer SMTP")
    sslPort = forms.CharField(max_length=200, label="Port SSL")
    email = forms.CharField(max_length=200, label="Użytkownik")
    password = forms.CharField(max_length=200, label="Hasło", widget=PasswordInput())
    
    class Meta:
        model = Email
        fields = ['smtp','sslPort','email','password']
