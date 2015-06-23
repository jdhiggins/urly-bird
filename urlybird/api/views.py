from django.shortcuts import render
from rest_framework import viewsets
from bookmark.models import Bookmark
from .serializer import BookmarkSerializer
from rest_framework import permissions
from api.permissions import IsOwnerOrReadOnly, OwnsRelatedBookmark

from bookmark.models import Bookmark
from click.models import Click
from api.serializer import BookmarkSerializer, ClickSerializer
from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import PermissionDenied
# Create your views here.

class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

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