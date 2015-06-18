from django.shortcuts import render
from .forms import UserCreationForm
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

# Create your views here.

def user_register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            password = user.password
            user.set_password(password)
            user.save()

            registered = True

            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Welcome, {}! You are now registered at MovieBase.".format(user.username)
            )
            return redirect('/index/')

    else:
        user_form = UserCreationForm()

    return render(request,
                  "bookmark/register.html",
                  {'user_creation_form': user_form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/index/')