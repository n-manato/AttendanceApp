from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import User
from .forms import LoginForm        #LoginFormのみ追加インポート
from django.contrib.auth import login as auth_login, logout as auth_logout


class Login(View):
    
   def get(self, request, *args, **kwargs):
       if request.user.is_authenticated:
            user=request.user
            if user.groups.filter(name='Student').exists():
                return redirect('/atbook/studentslist/')
            elif user.groups.filter(name__in=['HomeroomTeacher', 'SubjectTeacher']).exists():
                return redirect('/atbook/subject_list/')
            else:
                return redirect('/atbook/welcome/')  # デフォルトのリダイレクト先（所属グループが不明の場合）
       
       context = {'form': LoginForm()}
       return render(request, 'login.html', context)

   def post(self, request, *args, **kwargs):
       form = LoginForm(request.POST)
       if not form.is_valid():
           return render(request, 'login.html', {'form': form})
       user = form.get_user()
       auth_login(request, user)
       if user.groups.filter(name='Student').exists():
           return redirect('/atbook/studentslist/')
       elif user.groups.filter(name__in=['HomeroomTeacher', 'SubjectTeacher']).exists():
           return redirect('/atbook/subject_list/')
       else:
           return redirect('/atbook/welcome/')  # デフォルトのリダイレクト先（所属グループが不明の場合）
   


class Logout(View):
   def get(self, request, *args, **kwargs):
       if not request.user.is_authenticated:
           return redirect('/')
       auth_logout(request)
       return redirect('/')