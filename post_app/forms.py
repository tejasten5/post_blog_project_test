from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    email = forms.EmailField(max_length = 256,required=True,help_text = 'Enter Email')
    password = forms.CharField(max_length=100,required = True,help_text = 'Enter Password')

    def clean(self):
        data = self.cleaned_data
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise ValidationError("Email/Password is missing")

        try:
            user = User.objects.get(email = email)                        
        except Exception as e:
            raise ValidationError('Error')
        
        if not user or not user.check_password(password):           
            raise ValidationError("Email -- Password is missing")
        return data

# class RegisterUserForm(UserCreationForm):       

#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254,required=True,help_text='Required. Inform a valid email address.')

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email = email).exists():
#             raise ValidationError("You have forgotten about Fred!")
#         return email

#     class Meta:
#         model = User
#         fields = ('username','first_name','last_name','email', 'password1', 'password2', )

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length = 100,required=False,)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254,required=True,help_text='Required. Inform a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Password must match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError("This email is already registered")
        return email

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password',)

from . models import STATUS,Post
class CreatPostForm(forms.ModelForm):
    status = forms.CharField(max_length=2, widget=forms.Select(choices= STATUS))
    class Meta:
        fields = '__all__'
        model = Post
