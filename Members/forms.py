from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs={'class': '', 'type': 'text', 'placeholder': 'Логiн'}
        self.fields['first_name'].widget.attrs={'class': '', 'type': 'text', 'placeholder': 'Iмя'}
        self.fields['last_name'].widget.attrs={'class': '', 'type': 'text', 'placeholder': 'Прозвiшча'}
        self.fields['email'].widget.attrs={'class': '', 'type': 'email', 'placeholder': 'Электронная пошта'}
        self.fields['password1'].widget.attrs={'class': 'passwordInput', 'type': 'password', 'placeholder': 'Пароль'}
        self.fields['password2'].widget.attrs={'class': 'passwordInput', 'type': 'password', 'placeholder': 'Паўтарыце пароль'}

class RegisterProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)
    
    def __init__(self, *args, **kwargs):
        super(RegisterProfileForm, self).__init__(*args, **kwargs)

        # self.fields['bio'].label = 'О себе'
        self.fields['bio'].widget.attrs={'class': '', 'placeholder': 'Пра сябе', 'type': 'text'}