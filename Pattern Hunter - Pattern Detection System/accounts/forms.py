from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import LoginForm, SignupForm
from .models import User
from .models import Label
from django import forms


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class LabelCreationForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('User', 'data')

class LabelChangeForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('User', 'data')

class NewLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(NewLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your password'})

class NewSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(NewSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password again'})
