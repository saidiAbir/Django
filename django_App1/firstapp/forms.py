# forms.py

from django import forms
from .models import Author, BookSearch, Borrowing, DateSearch
from .models import Book
from .models import Student
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname']
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname']

class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ['student', 'book', 'date_borrowed', 'book_returned']
        date_borrowed = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],  # Add the desired format
    )
        widgets = {
            'date_borrowed': forms.DateTimeInput(attrs={'type': 'date'}),
        }
        


class BookSearchType(forms.ModelForm):
    class Meta:
        model = BookSearch
        fields = ['book']

    def __init__(self, *args, **kwargs):
        super(BookSearchType, self).__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all() 
        

class DateSearchType(forms.ModelForm):
    class Meta:
        model = DateSearch
        #fields = ['date_borrowed']
        fields = ['date_finn', 'date_fin']
        
    date_finn = forms.DateTimeField(
        label='Date de finn',
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],  # Format YYYY-MM-DD
    )
    date_fin = forms.DateTimeField(
        label='Date de fin',
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],  # Format YYYY-MM-DD
    )
    def __init__(self, *args, **kwargs):
        super(DateSearchType, self).__init__(*args, **kwargs)
        self.fields['date_finn'].queryset = Borrowing.objects.all()
        self.fields['date_fin'].queryset = Borrowing.objects.all()
