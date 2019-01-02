from __future__ import absolute_import

from django import forms
from .models import Post


from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.Form):
    title = forms.CharField(label='Tytuł postu:', max_length=200)
    text = forms.CharField(widget=CKEditorUploadingWidget(), label="Treść:")
    facebook = forms.BooleanField(label='Udostępnij przez Facebooka:', required=False)
    twitter = forms.BooleanField(label='Udostępnij przez Twittera:', required=False)
    published_date = forms.m(label='Data publikacji:')
    class Meta:
        model = Post
        fields = '__all__'
