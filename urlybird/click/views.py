from django.shortcuts import render
from .models import Bookmark, Click
from django.shortcuts import redirect
# Create your views here.


def click_tracker(request, short_id):
    bookmark = Bookmark.objects.get(short=short_id)
    click = Click()
    click.bookmark = bookmark
    click.address = request.META.get('REMOTE_ADDR', '')
    click.browser = request.META.get('HTTP_USER_AGENT', '')
    if request.user.is_authenticated():
        click.user = request.user.id
    click.save()
    return redirect(bookmark.long)


