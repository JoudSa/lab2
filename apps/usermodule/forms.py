from django import forms
from django.contrib.auth.models import User

class recoverForm(forms.Form):
    email = forms.EmailField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    password1 = forms.CharField(widget=forms.PasswordInput(), label="Password")  
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

