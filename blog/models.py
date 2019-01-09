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



class Google(models.Model):
    appId = models.CharField(max_length=200, verbose_name="identyfikator śledzenia")

    class Meta:
        verbose_name = 'Google Analitycs identyfikator śledzenia'
        verbose_name_plural = 'Google Analitycs identyfikator śledzenia'

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Google, self).save(*args, **kwargs)


    def __str__(self):
        return self.appId



class Facebook(models.Model):
    appId = models.CharField(max_length=200, verbose_name="identyfikator aplikacji")

    class Meta:
        verbose_name = 'Facebook identyfikator aplikacji'
        verbose_name_plural = 'Facebook identyfikator aplikacji'

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Facebook, self).save(*args, **kwargs)


    def __str__(self):
        return self.appId



class Settings(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nazwa bloga", default="Blog")
    post_color = models.CharField(max_length=200, verbose_name="Kolor tytułu postów", default="#007bff")
    navbar_color = models.CharField(max_length=200, verbose_name="Kolor paska nawigacji", default="#007bff")
    navbar_text_color = models.CharField(max_length=200, verbose_name="Kolor tekstu paska nawigacji", default="#ffffff" )
    about_enabled = models.BooleanField(default=False, verbose_name='Strona "o autorze" widoczna')
    contact_enabled = models.BooleanField(default=False, verbose_name='Strona "kontakt" widoczna')
    newsletter_enabled = models.BooleanField(default=False, verbose_name='Strona "newsletter" widoczna')
    custom_css = models.TextField(blank=True,max_length=10000, default="", verbose_name='Własny CSS (opcja dla zaawansowanych)')


    class Meta:
        verbose_name = 'Ustawienia'
        verbose_name_plural = 'Ustawienia'

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Settings, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


    def __str__(self):
        return "Ustawienia"



class Contact(models.Model):
    read = models.BooleanField(default=False, verbose_name='Przeczytana')
    created_date = models.DateField(default=timezone.now, verbose_name='Data wysłania')
    name = models.CharField(max_length=200, verbose_name="Autor", default="")
    email = models.CharField(max_length=200, verbose_name="Email", default="")
    text = models.TextField(max_length=2000, verbose_name="Wiadomość", default="")
  

    class Meta:
        verbose_name = 'Wiadomość'
        verbose_name_plural = 'Wiadomości'

    def add(self):
        self.save()

    def __str__(self):
        return  str(self.created_date) + " " + self.email + (" (Przeczytana)" if self.read else " (Nieprzeczytana)")



class About(models.Model):
    about = models.CharField(max_length=200000, verbose_name="O autorze", default="")

    class Meta:
        verbose_name = 'O autorze'
        verbose_name_plural = 'O autorze'

    def save(self, *args, **kwargs):
        self.pk = 1
        super(About, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


    def __str__(self):
        return "O autorze"


class Newsletter(models.Model):
    email = models.CharField(max_length=200, verbose_name="Email", default="")
    created_date = models.DateField(default=timezone.now, verbose_name='Data zapisania')
    confirmed = models.BooleanField(default=False, verbose_name="potwierdzono")
    code =  models.CharField(max_length=50, verbose_name="Kod potwierdzający", default="")
  

    class Meta:
        verbose_name = 'Zapisany do newslettera'
        verbose_name_plural = 'Zapisani do newslettera'

    def add(self):
        self.save()

    def __str__(self):
        return  self.email




class Email(models.Model):
    smtp = models.CharField(max_length=200, verbose_name="Serwer SMTP")
    sslPort = models.CharField(max_length=200, verbose_name="Port SSL")
    email = models.CharField(max_length=200, verbose_name="Użytkownik",)
    password = models.CharField(max_length=200, verbose_name="Hasło")

    class Meta:
        verbose_name = 'Konfiguracja serwera email'
        verbose_name_plural = 'Konfiguracja serwera email'

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Email, self).save(*args, **kwargs)


    def __str__(self):
        return 'Konfiguracja serwera email'

class Message(models.Model):
    title = models.CharField(verbose_name='Temat', max_length=200)
    text = models.TextField(max_length=20000, verbose_name="Zawartość")
    created_date = models.DateField(default=timezone.now, verbose_name='Data wysłania')

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletter'
    
    def __str__(self):
        return str(self.created_date) + " " + self.title
