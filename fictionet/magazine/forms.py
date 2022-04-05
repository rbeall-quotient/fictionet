from django import forms
from django.forms import models, ModelForm
from ckeditor.widgets import CKEditorWidget

from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

from magazine.models import Story


class StoryForm(ModelForm):
     class Meta:
         model = Story
         fields = ['title', 'subtitle', 'genre', 'content', 'tags']

