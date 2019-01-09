from django.contrib import admin
from .models import Post, Facebook, Google, Settings, Contact, Email, Newsletter, Message
from .forms import EmailForm


class EmailAdmin(admin.ModelAdmin):
    form = EmailForm

admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Facebook)
admin.site.register(Google)
admin.site.register(Email, EmailAdmin)
admin.site.register(Settings)

