from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django import forms
from .models import Task



class CreateUserForm(UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password Confirmation'

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
        }
          
        
class Loginform(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        field = ['title','content','id']
        exclude = ['user',]