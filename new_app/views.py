from django.shortcuts import render,redirect
from  . models import Student
from . forms import StudentForm


# Create your views here.

def index(request):
    student=Student.objects.all()
    return render(request,"index.html",{'student':student})
def add(request):
    if request.method=="POST":
        student_name=request.POST.get('student_name')
        mark1=request.POST.get('mark1')
        mark2=request.POST.get('mark2')
        mark3=request.POST.get('mark3')
        student=Student(student_name=student_name,mark1=mark1,mark2=mark2,mark3=mark3)
        student.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    student=Student.objects.get(id=id) 
    form=StudentForm(request.POST or None,instance=student)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'student':student})
def delete(request,id):
    if request.method=="POST":
        student=Student.objects.get(id=id)
        student.delete()
        return redirect('/')
    return render (request,'delete.html')
    