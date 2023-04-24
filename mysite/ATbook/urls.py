from django.urls import path
from . import views
from .views import indexc

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', indexc.as_view(), name='index2'),
]