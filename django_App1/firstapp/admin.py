# admin.py

from django.contrib import admin
from .models import Author, Book, Student, Borrowing

admin.site.register(Author)

admin.site.register(Book)


admin.site.register(Student)

    
admin.site.register(Borrowing)