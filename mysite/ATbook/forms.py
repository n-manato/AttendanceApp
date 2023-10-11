from django import forms 
from . import models

class AttendanceForm(forms.Form):
    product = forms.ModelChoiceField(models.Attend.objects, label='授業')
