from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth

from django.views.generic import DetailView, UpdateView
from regpage.models import User
from userpage.models import Profile


def home(request):
    user = request.user
    if user.username:
        return redirect('userpage:user-page', username = user.username)
    else:
        return redirect('accounts:login')