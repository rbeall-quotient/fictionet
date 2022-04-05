from django.urls import path, include

from . import views
from django.urls import path, include

app_name = 'magazine'
urlpatterns = [
    path('', views.index, name='index'),
    path('', include("django.contrib.auth.urls")),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit-profile'),
    path('story/edit', views.edit_story, name='edit-story'),
    path('story/edit/<int:pk>', views.edit_story, name='edit-story'),
]