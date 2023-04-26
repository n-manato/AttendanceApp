from django.urls import path
from . import views
from .views import home, AttendView,Attend_def

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', home.as_view(), name='home'),
    path('attend/', AttendView.as_view(), name='Attend'),
    path('attenddef/', Attend_def, name='Attenddef'),
]