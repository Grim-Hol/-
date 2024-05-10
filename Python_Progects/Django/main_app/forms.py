from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class EmailPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_reverse'].empty_label = 'Not choose'

    class Meta:
        model = Articles
        fields = ['title', 'author', 'body', 'status', 'data_reverse']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-input'}),
                   'body': forms.Textarea(attrs={'cols': 60, 'rows': 10}), }


class RegisterUser(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password1', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='password2', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {'username': forms.TextInput(attrs={'class': 'form-input'}),
                   'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
                   'password2': forms.PasswordInput(attrs={'class': 'form-input'})}


class AutentUser(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='password', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {'username': forms.TextInput(attrs={'class': 'form-input'}),
                   'password': forms.PasswordInput(attrs={'class': 'form-input'})}


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['main_text'].label = 'Your comment'

    class Meta:
        model = Comment
        fields = ['main_text']
        widgets = {'main_text': forms.TextInput(attrs={'class': 'form-input', 'rows': 10, 'cols': 10, })}
