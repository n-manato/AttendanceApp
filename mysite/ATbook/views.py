from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,AttendanceInfo
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy

def index(request):
    context = {"name":Student.objects.all()}
    return render(request,"ATbook/index.html",context)

class home(ListView):
    model = Student
    template_name = "ATbook/home.html"
    context_object_name = "home"

class AttendView(CreateView):
    template_name = 'ATbook/create.html'
    model = AttendanceInfo
    fields = '__all__'
    success_url = reverse_lazy('create')
    def get_initial(self):
          initial = super().get_initial()
          initial["Student"] = "山田太郎"
          return initial
    #Cannot resolve keyword 'name' into field. Choices are: attendance, attendance_id, date, id, student, student_id, teacher, teacher_id
def Attend_def(request):
    object = AttendanceInfo.objects.all()
    context = {'object': object}
    if request.method == 'POST':
        object.text = request.POST['Student.name']
        AttendanceInfo.objects.update_or_create(defaults={"Student.name":"null"})
    else:
        return render(request, 'ATbook/Attenddef.html', context)