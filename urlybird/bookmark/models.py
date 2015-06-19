from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.db.models import Avg, Count
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.urlresolvers import reverse
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
        return reverse('bookmark_update', kwargs={'pk': self.pk})
    #send it to bookmark-detail instead
    #

    ##overiding the save function in the class definition of bookmark
