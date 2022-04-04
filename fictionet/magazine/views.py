import os

from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
# Create your views here.
from fictionet import settings


def index(request):
    return render(request, 'magazine/index.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def profile(request):
    return render(request, 'magazine/profile.html')


def edit_profile(request):
    if request.method == 'GET':
        return render(request, 'magazine/profile_form.html')
    if request.method == 'POST':
        data = dict(request.POST.items())
        profile_pic = None

        fs = FileSystemStorage()

        for filename, file in request.FILES.items():
            profile_pic = request.FILES[filename]
            break

        if profile_pic is not None:
            if request.user.profile.profile_picture:
                request.user.profile.profile_picture.delete()
            extension = os.path.splitext(profile_pic.name)[1]
            fs.save(settings.MEDIA_ROOT + "/users/user_" + str(request.user.id) + "/profile" + extension, profile_pic)
            request.user.profile.profile_picture = "users/user_" + str(request.user.id) + "/profile" + extension

        if 'firstName' in data.keys():
            request.user.first_name = data['firstName']
        if 'lastName' in data.keys():
            request.user.last_name = data['lastName']
        if 'email' in data.keys():
            request.user.email = data['email']
        if 'phone' in data.keys():
            request.user.profile.phone_number = data['phone']
        if 'bio' in data.keys():
            request.user.profile.bio = data['bio']
        request.user.save()
        return HttpResponseRedirect(reverse('magazine:profile'))
