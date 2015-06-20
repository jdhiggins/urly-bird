from django.shortcuts import render
import operator
from django.db.models import Avg, Count
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.forms.models import model_to_dict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from django.forms import model_to_dict
from hashids import Hashids
import datetime
from django.utils import timezone


# Create your views here.

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Bookmark
from click.models import Click
from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class BookmarkCreate(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['long', 'title', 'description']
#    success_url = reverse_lazy('')

    def form_valid(self, form):
    #     #this is what happens when the formis valid
        form.instance.user = self.request.user
        hashids = Hashids(min_length = 4, salt="ArloBeaIdaKatie")
        previous = Bookmark.objects.latest('id')
        previousid = previous.id
        if previous.id is None:
            previousid = 0
        form.instance.short = hashids.encrypt(previousid + 1)

    # #     #super will save for you
        messages.add_message(self.request, messages.SUCCESS,"You created a bookmark!")
        return super(BookmarkCreate, self).form_valid(form)
        #can get rid of (BO


class BookmarkUpdate(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'description']
    template_name = 'bookmark/bookmark_update_form.html'
#    success_url = reverse_lazy('bookmark-detail')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS,"You updated your bookmark!")
        return super(BookmarkUpdate, self).form_valid(form)



class BookmarkDelete(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('index')



@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


class AllBookmarksListView(ListView):
    model = Bookmark
    queryset = Bookmark.objects.order_by('-created').all()
    paginate_by = 30
    context_object_name = 'bookmarks'


class UserBookmarksListView(ListView):
    model = Bookmark
    paginate_by = 30
    context_object_name = 'bookmarks'
    template_name = 'bookmark/user_display.html'

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Bookmark.objects.filter(user_id=user_id).order_by('-created')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(UserBookmarksListView, self).get_context_data(*args, **kwargs)
        context['user_to_display'] = User.objects.get(pk=self.kwargs['user_id'])
        return context


def display_bookmark(request, pk):
    bookmark = Bookmark.objects.get(pk=pk)

    number_clicks = Click.objects.filter(bookmark__id=pk).count()

    startdate = datetime.date.today() - datetime.timedelta(days=7)
    week_clicks = Click.objects.filter(bookmark__id=pk, time__gte=startdate).count()

    return render(request, "bookmark/bookmark_display.html",
                  {"bookmark": bookmark,
                   "number_clicks": number_clicks,
                   "week_clicks": week_clicks})


