from django.urls import path
from .views import *

app_name = "friends"

urlpatterns = [
    path('find-friends', FindFriendsListView.as_view(), name="find-friends"),
]

