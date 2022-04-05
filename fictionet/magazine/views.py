import os

from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import PermissionDenied
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
# Create your views here.
from fictionet import settings
from .forms import StoryForm
from .models import Story


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


def story(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'magazine/story.html', {'story': story})


def add_story(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = StoryForm(request.POST or None)
        # check whether it's valid:
        if form.is_valid():
            story = form.save(commit=False)
            story.author = request.user
            story.save()
            return HttpResponseRedirect(reverse("magazine:index"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = StoryForm()

    return render(request, 'magazine/storyform.html', {'form': form})


def edit_story(request, pk):
    story_instance = get_object_or_404(Story, pk=pk)
    print(story_instance.author.first_name)

    if story_instance.author.pk is not request.user.pk:
        raise PermissionDenied()

    form = StoryForm(request.POST or None, instance=story_instance)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # check whether it's valid:
        if form.is_valid():
            print(str(form.cleaned_data["tags"]))
            story = form.save(commit=False)
            tags = form.cleaned_data['tags']

            story.tags.clear()

            for tag in tags:
                story.tags.add(tag)

            story.save()
            return HttpResponseRedirect(reverse('magazine:story', args=(story.pk,)))

    return render(request, 'magazine/storyform.html', {'form': form, 'story': story_instance})