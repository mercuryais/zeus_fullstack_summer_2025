from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('author/', views.author_list, name='author_list'),
    path('member/', views.member_list, name='member_list'),
]