from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from bookmark.models import Bookmark
from django.db.models import Avg, Count
from django.core.exceptions import ValidationError
import datetime
from django.utils import timezone
import random
from faker import Faker
from hashids import Hashids
import pytz
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
    user = models.IntegerField(default=None, null=True)
    #to get user id if logged in, or None


def create_clicks(num_clicks):
    fake = Faker()

    for i in range(num_clicks):
        bookmarks = Bookmark.objects.all()
        bookmark = random.choice(bookmarks)
        click = Click()
        click.bookmark = bookmark
        user_list = User.objects.all()
        chance = random.random()
        if chance > .50:
            click.user = (random.choice(user_list)).pk
        else:
            click.user = 0
        unaware = fake.date_time_between(start_date="-1m", end_date="-1d")
        now_aware = unaware.replace(tzinfo=pytz.UTC)
        click.time = now_aware
        ip_list = [fake.ipv4() for i in range(100)]
        browser_list = [fake.user_agent() for i in range(250)]
        click.address = (random.choice(ip_list))
        click.browser = (random.choice(browser_list))
        click.save()