from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author, Member
from .forms import BookForm, AuthorForm, MemberForm
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

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'catalog/book_form.html', {'form': form})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'catalog/author_form.html', {'form': form})

def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'catalog/member_form.html', {'form': form})

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'catalog/book_form.html', {'form': form})

def delete_book(request ,pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    
    return render(request, 'catalog/book_confirm_delete.html', {'book': book})