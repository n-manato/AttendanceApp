from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.views.generic import ListView

def index(request):
    context = {"name":Student.objects.all()}
    return render(request,"ATbook/index.html",context)

class indexc(ListView):
    model = Student
    template_name = "ATbook/index2.html"
    context_object_name = "test"