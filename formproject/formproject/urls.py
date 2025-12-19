from django.urls import path
from formapp import views

urlpatterns = [
    path('', views.greeting, name='home'),
    path('about-us/', views.aboutUs, name='about_us'),
    path('page/<str:title>/', views.pages,name='page'),
    path('count/<int:num>/', views.count,name='count'),
    
]
