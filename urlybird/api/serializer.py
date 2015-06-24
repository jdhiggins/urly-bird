__author__ = 'joshuahiggins'
from rest_framework import serializers
from bookmark.models import Bookmark
from click.models import Click
from hashids import Hashids

from django.contrib.auth.models import User, Group


class ClickSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Click
        fields = ('bookmark', 'time', 'address', 'browser', 'user')


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    clicks = serializers.HyperlinkedIdentityField(view_name='click-list')
    #maybe?
    short = serializers.CharField(read_only=True)
#    url = serializers.HyperlinkedIdentityField(view_name='bookmark-detail')

    def create(self, validated_data):
            hashids = Hashids(min_length = 4, salt="ArloBeaIdaKatie")
            previous = Bookmark.objects.latest('id')
            previousid = previous.id
            if previous.id is None:
                previousid = 0
            bookmark = Bookmark.objects.create(**validated_data)
            bookmark.short = hashids.encrypt(previousid + 1)
            bookmark.save()
            return bookmark

    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'long', 'description', 'title', 'url', 'short', 'created', 'number_clicks', 'edited',
                  'clicks')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

