from django.shortcuts import render

def student_list(request):
    students = ['Anu', 'Rahul', 'Meena']
    welcome = "Welcome Students"
    return render(request, 'studentsapp/students.html', {
        'students': students,
        'welcome': welcome
    })
def home(request):
    return render(request, 'studentsapp/home.html')

