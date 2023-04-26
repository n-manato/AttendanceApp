from django import forms 
from .models import AttendanceInfo

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceInfo
        fields = {'id','student','teacher','attendance'}
        widgets = {
            'id':forms.NumberInput(),
            'student': forms.TextInput(),
            'teacher': forms.TextInput(),
            'attendance': forms.TextInput(),
        }
        labels = {
            'id':'番号',
            'student':'生徒の名前',
            'teacher':'先生の名前',
            'attendance':'出欠席情報'
        }