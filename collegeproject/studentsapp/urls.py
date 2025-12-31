from django.urls import path
from . import views

app_name = 'studentsapp'

urlpatterns = [
     path('', views.home, name='home'),
    path('students/', views.student_list, name='list'),
]
