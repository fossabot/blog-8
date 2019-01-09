from .models import Settings, About, Email, Contact
from .common import getGoogleScript

def settings(request):
    About.load()
    messages = len( Contact.objects.filter(read=False).values_list('email', flat=True))
    email = True if len( Email.objects.values_list('smtp', flat=True))>0 else False
    return {'settings': Settings.load(), 'google' : getGoogleScript(), 'email_configured' : email, 'new_messages' : messages }