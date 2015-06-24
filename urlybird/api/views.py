from django.shortcuts import render
from rest_framework import viewsets
from bookmark.models import Bookmark
from .serializer import BookmarkSerializer
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly, OwnsRelatedBookmark
from django.contrib.auth.models import User
from bookmark.models import Bookmark
from click.models import Click
from api.serializer import BookmarkSerializer, ClickSerializer, UserSerializer
from rest_framework import viewsets, permissions, generics, filters
from rest_framework.exceptions import PermissionDenied
import django_filters
# Create your views here.


class BookmarkFilter(django_filters.FilterSet):
    long = django_filters.CharFilter(name="long", lookup_type="icontains")
    title = django_filters.CharFilter(name="title", lookup_type="icontains")
    description = django_filters.CharFilter(name="title", lookup_type="icontains")

    class Meta:
        model = Bookmark
        fields = ['long', 'title', 'description']



class BookmarkViewSet(viewsets.ModelViewSet):
    """Search title, description or long in the style http://localhost:8000/api/bookmarks/?title=mortar"""
    # queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    #change to IsAuthenticated, drop OrReadOnly
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BookmarkFilter

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ClickListView(generics.ListAPIView):
    serializer_class = ClickSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_queryset(self):
        bookmarkpk = self.kwargs['pk']
        return Click.objects.filter(bookmark__pk=bookmarkpk)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class ClickCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ClickSerializer

    def perform_create(self, serializer):
        bookmark = serializer.validated_data['bookmark']
        if self.request.user != bookmark.user:
            raise PermissionDenied
        serializer.save()


class ClickDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          OwnsRelatedBookmark)
    serializer_class = ClickSerializer
    queryset = Click.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    