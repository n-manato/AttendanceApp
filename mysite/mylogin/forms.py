from django import forms
from .models import User


#追加インポート
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField
from django.core.exceptions import ObjectDoesNotExist


#LoginFormの追記
class LoginForm(forms.Form):

   username = UsernameField(
       label='ユーザー名',
       max_length=255,
       widget=forms.TextInput(
           attrs={'placeholder': 'username', 'autofocus': True,'class': 'form-control form-control-lg bg-dark text-white'}),
   )

   password = forms.CharField(
       label='パスワード',
       strip=False,
       widget=forms.PasswordInput(
           attrs={'placeholder': 'password','class': 'form-control form-control-lg bg-dark text-white'}, render_value=True),
   )

   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.user_cache = None

   def clean_password(self):
       value = self.cleaned_data['password']
       return value

   def clean_username(self):
       value = self.cleaned_data['username']
       if len(value) < 3:
           raise forms.ValidationError(
               'Plese enter at last %(min_length)s characters', params={'min_length': 3})
       return value

   def clean(self):
       username = self.cleaned_data.get('username')
       password = self.cleaned_data.get('password')
       try:
           user = get_user_model().objects.get(username=username)
       except ObjectDoesNotExist:
           raise forms.ValidationError("Please enter a valid username")
       if not user.check_password(password):
           raise forms.ValidationError("Please enter the correct username and password")
       self.user_cache = user

   def get_user(self):
       return self.user_cache
   

