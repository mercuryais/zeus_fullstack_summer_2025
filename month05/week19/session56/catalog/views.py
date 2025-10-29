from django.shortcuts import render
from .models import Book, Author, Member

def book_list(request):
    books = Book.objects.all()
    context = {
        'books_key': books
    }
    return render(request, 'catalog/book_list.html', context=context)

def author_list(request):
    authors = Author.objects.all()
    context = {
        'author_key': authors
    }
    return render(request, 'catalog/author_list.html', context=context)

def member_list(request):
    members = Member.objects.all()
    context = {
        'member_key': members
    }
    return render(request, 'catalog/member_list.html', context=context)
