from django.shortcuts import render

def teacher_list(request):
    teachers = ['Mr. Kumar', 'Ms. Priya']
    welcome = "Welcome Teachers"
    return render(request, 'teachersapp/teachers.html', {
        'teachers': teachers,
        'welcome': welcome
    })

