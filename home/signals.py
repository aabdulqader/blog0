from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in



# https://docs.djangoproject.com/en/3.1/ref/request-response/
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip
    print('sdfgdfgfdgfg', ip)
