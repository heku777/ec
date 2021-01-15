from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Profile
from django.views import generic


class Profile_View(generic.ListView):
    model = Profile
    template_name = 'accounts/profile.html'

