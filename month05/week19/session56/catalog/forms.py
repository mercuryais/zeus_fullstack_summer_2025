from django import forms
from .models import Book, Author, Member

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author_name', 'published_date', 'isbn']
        labels = {
            'title': 'Номын нэр',
            'author_name': 'Зохиогчийн нэр', 
            'published_date': 'Хэвлэгдсэн огноо (MM/DD/YYYY)', 
            'isbn': 'ISBN дугаар'
        }
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'biography']
        labels = {
            'name': 'Зохиогчийн нэр',
            'birth_date': 'Зохиогчийн төрсөн өдөр (MM/DD/YYYY)',
            'biography': 'Био'
        }
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email']
        labels = {
            'name': 'Гишүүний нэр',
            'email': 'Гишүүний имэйл'
        }