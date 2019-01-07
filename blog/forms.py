from __future__ import absolute_import

from django import forms
from .models import Post


from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from bootstrap_datepicker_plus import DatePickerInput
from datetime import datetime

class PostForm(forms.Form):
    title = forms.CharField(label='Tytuł postu:', max_length=200, widget=forms.TextInput())
    published_date = forms.DateField(input_formats=['%d/%m/%Y'], label='Data publikacji:',  widget=DatePickerInput(format='%d/%m/%Y'))
    text = forms.CharField(widget=CKEditorUploadingWidget(), label="")
    facebook = forms.BooleanField(label='Udostępnij przez Facebooka:', required=False)
    twitter = forms.BooleanField(label='Udostępnij przez Twittera:', required=False)
    comments = forms.BooleanField(label='Włącz komentarze:', required=False)
 
    class Meta:
        model = Post
        fields = '__all__'
