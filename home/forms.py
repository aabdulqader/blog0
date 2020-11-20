from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post




class AddPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'title': 'Title',
            'desc' : 'Description'
        }
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Title'

            }),
            'desc':forms.Textarea(attrs={
                'class':'form-control', 
                'placeholder': 'Write Your Post'
            })
        }











class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'********'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'********'}))
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'username':'Username',
            'email': 'Email',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Fist Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Last Name'}),
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Username'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Valid Email'}),
            
        }


#authentication form for login
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(attrs={
        'autocomplete':'current-password', 'class':'form-control', 'placeholder':'********',
    }))


