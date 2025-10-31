from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('author/', views.author_list, name='author_list'),
    path('member/', views.member_list, name='member_list'),
    path('book/new/', views.create_book, name='book_create'),
    path('author/new/', views.create_author, name='author_create'),
    path('member/new/', views.create_member, name='member_create')
]