from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.product_create, name='createproduct'),
    path('retrieve/', views.product_read, name='retrieveproduct'),
    path('<int:pk>/pdf/', views.generate_pdf, name='generate_pdf'),
    path('send_product_email/<int:pk>/', views.send_product_email, name='send_product_email'),
]
