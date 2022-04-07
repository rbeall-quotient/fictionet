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


class Submission(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField()
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Story(Submission):
    subtitle = models.CharField(max_length=200, blank=True)
    ratings = GenericRelation(Rating, related_query_name='storys')

    class Genre(models.TextChoices):
        LIT_FIC = 'LF', _('Literary Fiction')
        SCI_FI = 'SF', _('Science Fiction')
        FAN = 'F', _('Fantasy')
        HRR = 'HR', _('Horror')
        MYS = 'MYS', _('Mystery')
        HIS = 'HIS', _('Historical Fiction')
        ROM = 'ROM', _('Romance')

    genre = models.CharField(
        max_length=3,
        choices=Genre.choices,
        default=Genre.LIT_FIC,
    )


class Favorite(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'story',)

    def __str__(self):
        return self.name

