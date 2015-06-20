"""urlybird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from bookmark import views as bookmark_views
from django.conf.urls import url
from bookmark.views import BookmarkCreate, BookmarkUpdate, BookmarkDelete
from click import views as click_views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url('^register/', CreateView.as_view(
            template_name='bookmark/register.html',
            form_class=UserCreationForm,
            success_url='index/'), name = "user_register"
    ),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^index/$', TemplateView.as_view(template_name='bookmark/index.html'),name = 'index'),
    url(r'bookmark/add/$', BookmarkCreate.as_view(), name='bookmark_add'),
    url(r'bookmark/(?P<pk>[0-9]+)/$', BookmarkUpdate.as_view(), name='bookmark-update'),
    url(r'bookmark/(?P<pk>[0-9]+)/delete/$', BookmarkDelete.as_view(), name='bookmark_delete'),
    url(r'bookmark/detail/(?P<pk>[0-9]+)/$', bookmark_views.display_bookmark, name='bookmark-detail'),
    url(r'bookmark/logout/$', bookmark_views.user_logout, name="logout"),
    url(r'^bookmark/all_bookmarks$', bookmark_views.AllBookmarksListView.as_view(), name='all_bookmarks'),
    url(r'^bookmark/user_display/(?P<user_id>[0-9]+)$', bookmark_views.UserBookmarksListView.as_view(),
        name="user_display"),
    url(r'b/(?P<short_id>[A-Za-z0-9]+)/', click_views.click_tracker, name='click_tracker'),

]
