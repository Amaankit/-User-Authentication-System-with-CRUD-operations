from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class UserSignUp(UserCreationForm):
  #  password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput, )#label_suffix=' '
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),label_suffix=' ')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name',label_suffix=' ')
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name',label_suffix=' ',required=False)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address',label_suffix=' ')
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),label_suffix=' ',help_text="helo")
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),label_suffix=' ',help_text="helo")
    
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
        label_suffix={'username':' '}
class EditUserForm(UserChangeForm):
    password=None
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name',label_suffix=' ')
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address',label_suffix=' ')
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','last_login','date_joined']
        labels={'email':'Email'}
        help_text={'password':'helo'}

class EditAdminForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['password'].help_text = "Raw passwords are not stored, so there is no way to see this user’s password, but you can change the password using  "
    
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name',label_suffix=' ')
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address',label_suffix=' ')
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email'}
        