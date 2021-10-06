from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# registration form that inherits from user creation form 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Meta class, anytime this class is instantiated it is of type (model) User
    class Meta:
        # fields for instsance of this User class
        model = User
        fields = ['username', 'email', 'password1', 'password2']