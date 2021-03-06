from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.db.models import Avg, Count
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.urlresolvers import reverse
import random
from faker import Faker
from hashids import Hashids
import pytz
# Create your models here.

class Bookmark(models.Model):
    user = models.ForeignKey(User)
    long = models.URLField(max_length=255)
    short = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default=None)
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(default=timezone.now)

    # def save(self, *args, *kwargs):


    def get_absolute_url(self):
        return reverse('bookmark-detail', kwargs={'pk': self.pk})
    #send it to bookmark-detail instead
    #

    @property
    def number_clicks(self):
        return self.click_set.count()

    ##overiding the save function in the class definition of bookmark


def create_users(num_users):
    for i in range(num_users):
        user = User.objects.create_user('User{}'.format(i),
                                        'user{}@example.com'.format(i),
                                        'password')
        password = "password"
        user.set_password(password)
        user.save()


def create_bookmarks(num_bookmarks):
    fake = Faker()
    hashids = Hashids(min_length = 4, salt="ArloBeaIdaKatie")
    for i in range(num_bookmarks):
        bookmark = Bookmark()
        users = User.objects.all()
        bookmark.user = random.choice(users)
        bookmark.long = fake.uri()
        bookmark.short = hashids.encrypt(i)
        bookmark.title = fake.bs()
        bookmark.description = fake.catch_phrase()
        unaware = fake.date_time_between(start_date="-4m", end_date="-2m")
        now_aware = unaware.replace(tzinfo=pytz.UTC)
        bookmark.created = now_aware
        bookmark.edited = now_aware
        bookmark.save()
