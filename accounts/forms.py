from accounts.models import Profile
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username=forms.CharField(label='Nom utilisateur',widget=forms.TextInput(
        attrs={
            'placeholder':'Entrer le nom',
            'class':'form-control'
        }
    ))
    password=forms.CharField(label='Mot de passe',widget=forms.PasswordInput(
        attrs={
            'placeholder':'M. passe',
            'class':'form-control'
        }
    ))
    

class RegisterForm(UserCreationForm):
    username=forms.CharField(label='Nom utilisateur',widget=forms.TextInput(
        attrs={
            'placeholder':'Entrer le nom',
            'class':'form-control'
        }
    ))
    email=forms.CharField(label='Votre Email',widget=forms.EmailInput(
        attrs={
            'placeholder':'Email',
            'class':'form-control',
            'type':'email'
        }
    ))
    password1=forms.CharField(label='Mot de passe',widget=forms.PasswordInput(
        attrs={
            'placeholder':'M. passe',
            'class':'form-control'
        }
    ))
    password2=forms.CharField(label='Cnf M.passe',widget=forms.PasswordInput(
        attrs={
            'placeholder':'Mot de passe',
            'class':'form-control'
        }
    ))
    class Meta:
        model=User 
        fields=['username','email','password1','password2']
        
class ProfileForm(forms.ModelForm):
    birthday=forms.DateField(label='Date de Naissance',widget=forms.DateInput(
        attrs={
            'placeholder':'M. passe',
            'class':'form-control',
            'type':'date'
        }
    ))
    phone=forms.IntegerField(label='Téléphone',widget=forms.NumberInput(
        attrs={
            'placeholder':'Mot de passe',
            'class':'form-control',
            'type':'number'
        }
    ))
    class Meta:
        model=Profile
        fields=['birthday','phone']
    