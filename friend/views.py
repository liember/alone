from django.shortcuts import render
from .models import *
from django.views.generic import ListView
# Create your views here.

class FindFriendsListView(ListView):
    model = Friend
    context_object_name = 'users'
    template_name = "friend/find-friends.html"

    def get_queryset(self):
        current_user_friends = self.request.user.friends.values('id')
        sent_request = list(Friend.objects.filter(user=self.request.user).values_list('friend_id', flat=True))
        users = User.objects.exclude(id__in=current_user_friends).exclude(id__in=sent_request).exclude(id=self.request.user.id)
        return users