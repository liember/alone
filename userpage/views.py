from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth


# Create your views here.

from .models import UserInfo


def hello(request):
    user = request.user
    if user.username != '':
        return HttpResponse("Hello " + user.username)
    else:
        return HttpResponse("Who are you?" )