import os

from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth.models import User
from django.http import request
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from star_ratings.models import Rating

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from taggit.managers import TaggableManager

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    extension = os.path.splitext(filename)[1]
    return 'users/user_{0}/{1}'.format(instance.user.id, 'profile' + extension)

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = PhoneNumberField(blank=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)
        instance.profile.save()