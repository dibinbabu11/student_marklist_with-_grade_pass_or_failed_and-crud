from . models import Student 
from django import forms
class StudentForm(forms.ModelForm):
    
    class Meta:
        model=Student
        fields = ['student_name','mark1','mark2','mark3']
