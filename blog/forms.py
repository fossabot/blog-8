from __future__ import absolute_import

from django import forms
from .models import Post


from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.Form):
 content = forms.CharField(widget=CKEditorUploadingWidget())
 class Meta:
        model = Post
        fields = '__all__'
