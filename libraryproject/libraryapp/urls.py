from django.urls import path
from .views import add_book, book_list

urlpatterns = [
    path('add/', add_book, name='add_book'),
    path('books/', book_list, name='book_list'),
]
