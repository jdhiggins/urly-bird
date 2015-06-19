from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from bookmark.models import Bookmark
from django.db.models import Avg, Count
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.

class Click(models.Model):
    bookmark = models.ForeignKey(Bookmark)
    time = models.DateTimeField(default=timezone.now)
    address = models.CharField(max_length=500, default=None)
    #request.META.get('REMOTE_ADDR', '')
    #or django ip-ware
    # #    from ipware.ip import get_real_ip
    # ip = get_real_ip(request)
    # if ip is not None:
    #    # we have a real, public ip address for user
    # else:
    #    # we don't have a real, public ip address for user
    browser = models.CharField(max_length=500, default=None)
    #request.META.get('HTTP_USER_AGENT', '')
    # >>> t = Template("{{ request.META.HTTP_REFERER }}")
    user = models.IntegerField(default=None)
    #to get user id if logged in, or None


