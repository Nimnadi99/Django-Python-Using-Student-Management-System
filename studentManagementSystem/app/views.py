from django.shortcuts import render, redirect
from .models import Student
from django.http import JsonResponse
from .forms import StudentForm
from .models import Student
# Create your views here.

# retriew and display all of the students records
def student_list(request):
    context = {'student_list' :Student.objects.all().order_by('id')}
    return render(request, 'student_list.html', context)

# GET & POST request for insert and update operations
def student_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance= student)
        return render(request, "student_form.html", {'form': form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance =student)
        if form.is_valid():
            form.save()
        return redirect('/student/list')
    
# Delete student request handle
def student_delete(request, id=0):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('/student/list')