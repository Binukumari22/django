from django.urls import path
from . import views

app_name = 'teachersapp'

urlpatterns = [
    path('', views.teacher_list, name='list'),
]
