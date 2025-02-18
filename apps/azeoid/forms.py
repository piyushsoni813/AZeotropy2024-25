from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AzeoProfile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class AzeoProfileForm(forms.ModelForm):
    class Meta:
        model = AzeoProfile
        fields = ['college', 'department', 'year_of_study', 'phone']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = AzeoProfile
        fields = ['college', 'department', 'year_of_study', 'phone']