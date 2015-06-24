__author__ = 'joshuahiggins'
from rest_framework import serializers
from bookmark.models import Bookmark
from click.models import Click


class ClickSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Click
        fields = ('bookmark', 'time', 'address', 'browser', 'user')


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    clicks = serializers.HyperlinkedIdentityField(view_name='click-list')
    #maybe?
    url = serializers.HyperlinkedIdentityField(view_name='bookmarks-api-detail')
    class Meta:
        model = Bookmark
        fields = ('id', 'user', 'long', 'description', 'title', 'url', 'short', 'created', 'number_clicks', 'edited',
                  'clicks')