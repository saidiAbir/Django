# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the firstapp index.")

# views.py

from django.shortcuts import render,get_object_or_404, redirect
from django.views import View 
from django.db.models import Count
from .models import Author, BookSearch, Borrowing, DateSearch, Student
from .forms import AuthorForm, BookSearchType, BorrowingForm, DateSearchType, StudentForm
from .models import Book
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
class AuthorCreateView(View):
    template_name = 'create_author.html'

    def get(self, request):
        form = AuthorForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')  
        return render(request, self.template_name, {'form': form})
class AuthorListView(View):
    template_name = 'author_list.html'

    def get(self, request):
        authors = Author.objects.all()
        return render(request, self.template_name, {'authors': authors})
    
class AuthorShowView(View):
    template_name = 'author_show.html'

    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        return render(request, self.template_name, {'author': author})
    def post(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return redirect('author_list') 
class AuthorEditView(View):
    template_name = 'edit_author.html'

    def get(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        form = AuthorForm(instance=author)
        return render(request, self.template_name, {'form': form, 'author': author})

    def post(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')  
        return render(request, self.template_name, {'form': form, 'author': author})
    
class StudentCreateView(View):
    template_name = 'student_create.html'

    def get(self, request):
        form = StudentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  
        return render(request, self.template_name, {'form': form})
class StudentListView(View):
    template_name = 'student_list.html'

    def get(self, request):
        students = Student.objects.all()
        return render(request, self.template_name, {'Students': students})
    
class StudentShowView(View):
    template_name = 'student_show.html'

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        return render(request, self.template_name, {'student': student})
   
class StudentEditView(View):
    template_name = 'student_edit.html'

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(instance=student)
        return render(request, self.template_name, {'form': form, 'student': student})

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  
        return render(request, self.template_name, {'form': form, 'student': student})
    
class StudentDeleteView(View):
    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return redirect('student_list') 
    

class BookListView(View):
    template_name = 'book_list.html'

    def get(self, request):
        books = Book.objects.all()
        return render(request, self.template_name, {'books': books})

class BookCreateView(View):
    template_name = 'create_book.html'

    def get(self, request):
        form = BookForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  
        return render(request, self.template_name, {'form': form})
    

class BookShowView(View):
    template_name = 'book_show.html'

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, self.template_name, {'book': book})
    

class BookEditView(View):
    template_name = 'edit_book.html'

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, self.template_name, {'form': form, 'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  
        return render(request, self.template_name, {'form': form, 'book': book})
    
class BookDeleteView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('book_list') 
    

# Borrowing
# List View
class BorrowingListView(View):
    def get(self, request):
        borrowings = Borrowing.objects.all()
        return render(request, 'borrowing_list.html', {'borrowings': borrowings})

# Create View
class BorrowingCreateView(View):
    def get(self, request):
        form = BorrowingForm()
        return render(request, 'borrowing_create.html', {'form': form})

    def post(self, request):
        form = BorrowingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrowing_list')
        return render(request, 'borrowing_create.html', {'form': form})

# Show View
class BorrowingShowView(View):
    def get(self, request, pk):
        borrowing = get_object_or_404(Borrowing, pk=pk)
        return render(request, 'borrowing_show.html', {'borrowing': borrowing})

# Edit View
class BorrowingEditView(View):
    def get(self, request, pk):
        borrowing = get_object_or_404(Borrowing, pk=pk)
        form = BorrowingForm(instance=borrowing)
        return render(request, 'borrowing_edit.html', {'form': form, 'borrowing': borrowing})

    def post(self, request, pk):
        borrowing = get_object_or_404(Borrowing, pk=pk)
        form = BorrowingForm(request.POST, instance=borrowing)
        if form.is_valid():
            form.save()
            return redirect('borrowing_list')
        return render(request, 'borrowing_edit.html', {'form': form, 'borrowing': borrowing})

# Delete View
class BorrowingDeleteView(View):
    def post(self, request, pk):
        borrowing = get_object_or_404(Borrowing, pk=pk)
        borrowing.delete()
        return redirect('borrowing_list')
#findMostPopularBooks
class  findMostPopularBooks(View):
    def get(self,request):
        most_popular_books = Borrowing.objects.values('book__title').annotate(how_many=Count('book')).order_by('-how_many')
        return render(request,'report.html',{'most':most_popular_books})
def borrowing_book(request):
    date_search = DateSearch()

    borrowings = []  # Initialisation de borrowings

    if request.method == 'POST':
        form = DateSearchType(request.POST, instance=date_search)
        if form.is_valid():
            date_finn = form.cleaned_data['date_finn']
            date_fin = form.cleaned_data['date_fin']
            borrowings = Borrowing.objects.filter(date_borrowed__range=[date_finn, date_fin])
    else:
        form = DateSearchType(instance=date_search)

    return render(request, 'BorrowingBook.html', {'form': form, 'borrowings': borrowings})

#register

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
#login
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')  # Replace 'home' with the name of your homepage URL
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
#logout
def logout(request):
    auth_logout(request)
    return redirect('login')