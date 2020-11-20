from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.core.cache import cache



# https://docs.djangoproject.com/en/3.1/ref/request-response/
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip
    login_count = cache.get('count', 0, version=user.pk)
    newcount = login_count + 1
    cache.set('count', newcount, 60*60*24, version=user.pk)
