from django.urls import path
from .views import Attend_def, Teachers_list, Students_list, welcome_view, Subject_list, Double_slider, Teachers_list2

app_name = "ATbook"

urlpatterns = [
    path('welcome/', welcome_view, name='welcome'),
    path('studentslist/', Students_list, name='Studentslist'),
    path('teacherslist/', Teachers_list, name='Teacherslist'),
    path('teacherslist2/', Teachers_list2, name='Teacherslist2'),
    path('attenddef/', Attend_def, name='Attenddef'),
    path('subject_list/', Subject_list, name='Subject_list'),
    path('double_slider/', Double_slider, name='Double_slider'),
]
