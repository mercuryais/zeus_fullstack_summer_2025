from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Book name")
    author_name = models.CharField(max_length=200, verbose_name="Author Name")
    published_date = models.DateField(verbose_name="Published Date")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN Number")

    def __str__(self):
        return self.title
class Author(models.Model):
    name  = models.CharField(max_length=100, verbose_name="Name")
    birth_date = models.DateField(verbose_name="Birthday")
    biography = models.TextField(blank=True, null=True, verbose_name="Biography")

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100, verbose_name="Member Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    join_Date = models.DateField(auto_now_add=True, verbose_name="Registered Day")

    def __str__(self):
        return self.name