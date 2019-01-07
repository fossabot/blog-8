from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Autor')
    title = models.CharField(max_length=200, verbose_name='Tytuł')
    text = models.TextField(verbose_name='Treść')
    facebook = models.BooleanField(default=False, verbose_name='Facebook')
    twitter = models.BooleanField(default=False, verbose_name='Twitter')
    comments = models.BooleanField(default=False, verbose_name='Komentarze')
    created_date = models.DateField(default=timezone.now, verbose_name='Data utworzenia')
    published_date = models.DateField(blank=True, null=True,  verbose_name='Data opublikowania')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posty'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Facebook(models.Model):
    appId = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Facebook Id'
        verbose_name_plural = 'Facebook Id'

    def add(self):
        self.save()

    def __str__(self):
        return self.appId