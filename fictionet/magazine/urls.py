from django.urls import path, include

from . import views
from django.urls import path, include

app_name = 'magazine'
urlpatterns = [
    path('', views.index, name='index'),
    path('', include("django.contrib.auth.urls")),
    path("signup/", views.SignUp.as_view(), name="signup"),
]