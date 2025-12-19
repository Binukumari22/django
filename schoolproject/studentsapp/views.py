from django.shortcuts import render


results = {
    'Anu': 'Pass',
    'Rahul': 'Fail',
    'Meena': 'Distinction'
}

def home(request):
    students = results.keys()
    return render(request, 'studentsapp/home.html', {'students': students})

def result(request, name):
    res = results.get(name, 'Result not found')
    return render(request, 'studentsapp/result.html', {
        'name': name,
        'result': res
    })

