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
    path('story/add', views.add_story, name='add-story'),
    path('story/<int:pk>', views.story, name='story'),
    path('story/edit/<int:pk>', views.edit_story, name='edit-story'),
]