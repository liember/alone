from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth

from django.views.generic import DetailView, UpdateView, View
from regpage.models import User
from userpage.models import Profile

class UserView(DetailView):
    model = User
    template_name = "profile/user-profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "user"
    object = None

    def get_object(self, queryset=None):
        return self.model.objects.select_related('profile').get(username=self.kwargs.get(self.slug_url_kwarg))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        # print(type(self.object))
        return self.render_to_response(context)


def hello(request):
    user = request.user
    if user.username != '':
        return HttpResponse("Hello " + user.username)
    else:
        return HttpResponse("Who are you?" )