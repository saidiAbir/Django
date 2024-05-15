# models.py

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    def __str__(self):
        return f" book: {self.title}"


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Borrowing(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_borrowed = models.DateField()
    book_returned = models.BooleanField()

    def __str__(self):
        return f"{self.student} borrowed {self.book} on {self.date_borrowed}"
class BookSearch(models.Model):
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.book)
    
    
#class DateSearch(models.Model):
  #  date_borrowed = models.DateField()

   # def __str__(self):
    #    return str(self.date_borrowed)
    
class DateSearch(models.Model):
    date_finn = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"{self.date_finn} - {self.date_fin}"
