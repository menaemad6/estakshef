from django import forms
from . import models
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'username','email']



class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['name', 'image' , 'phone' , 'country']





