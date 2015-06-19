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


# Create your views here.

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Bookmark
from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class BookmarkCreate(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['long', 'title', 'description']

    def form_valid(self, form):
    #     #this is what happens when the formis valid
        form.instance.user = self.request.user
    # #     hashids = Hashids(min_length = 4, salt="ArloBeaIdaKatie")
    # #     previous = Bookmark.objects.latest('id')
    # #     previousid = previous.id
    # #     if previous.id is None:
    # #         previousid = 0
    # #     form.instance.short = hashids.encrypt(previousid + 1)
    # #
    # #     #super will save for you
        return super(BookmarkCreate, self).form_valid(form)
        #can get rid of (BO


class BookmarkUpdate(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'description']
    # template_name = 'bookmark/'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
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
    paginate_by = 30
    context_object_name = 'bookmarks'