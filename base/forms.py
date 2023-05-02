from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Tasks

class SignupForm(UserCreationForm):

    username = forms.CharField(widget=forms.TimeInput(attrs={"placeholder": "Create Username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Create Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Re-enter Password"}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your task here'}))

    class Meta:
        model = Tasks
        fields = ['title', 'completed']