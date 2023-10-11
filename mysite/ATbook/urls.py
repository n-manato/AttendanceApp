from django.urls import path
from .views import Attend_def,Teachers_list,Students_list,welcome_view,Subject_list,Double_slider

app_name = "ATbook"

urlpatterns = [
    path('welcome/', welcome_view, name='welcome'),
    path('studentslist/', Students_list, name='Studentslist'),
    path('teacherslist/', Teachers_list, name='Teacherslist'),
    path('attenddef/', Attend_def, name='Attenddef'),
    path('subject_list/', Subject_list, name='Subject_list'),
    path('double_slider/', Double_slider, name='Double_slider'),
]