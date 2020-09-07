from django import forms

from .models import TingerProfile

class TingerProfileForm (forms.ModelForm):
  class Meta:
    model = TingerProfile
    fields = ('avatar',)