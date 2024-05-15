from django.urls import path
from django.shortcuts import redirect
from .views import AuthorCreateView,AuthorListView,AuthorEditView,AuthorShowView,BookEditView,BookShowView,BookListView,BookCreateView,BookDeleteView, BorrowingCreateView, BorrowingDeleteView, BorrowingEditView, BorrowingListView, BorrowingShowView, StudentCreateView, StudentDeleteView, StudentEditView, StudentListView, StudentShowView, borrowing_book, findMostPopularBooks
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',lambda request: redirect('authors/', permanent=True)),
    path('author/create', AuthorCreateView.as_view(), name='create_author'),
     path('authors/', AuthorListView.as_view(), name='author_list'),
      path('author/show/<int:pk>/', AuthorShowView.as_view(), name='author_show'),
    path('author/edit/<int:pk>/', AuthorEditView.as_view(), name='author_edit'),
     path('book/create/', BookCreateView.as_view(), name='create_book'),
    path('book/list/', BookListView.as_view(), name='book_list'),
    path('book/show/<int:pk>/', BookShowView.as_view(), name='book_show'),
    path('book/edit/<int:pk>/', BookEditView.as_view(), name='book_edit'),
     path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
      path('students/', StudentListView.as_view(), name='student_list'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/show/<int:pk>/', StudentShowView.as_view(), name='student_show'),
    path('students/edit/<int:pk>/', StudentEditView.as_view(), name='student_edit'),
     path('student/delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
    path('borrowings/', BorrowingListView.as_view(), name='borrowing_list'),
    path('borrowings/create/', BorrowingCreateView.as_view(), name='borrowing_create'),
    path('borrowings/show/<int:pk>/', BorrowingShowView.as_view(), name='borrowing_show'),
    path('borrowings/edit/<int:pk>/', BorrowingEditView.as_view(), name='borrowing_edit'),
    path('borrowings/delete/<int:pk>/', BorrowingDeleteView.as_view(), name='borrowing_delete'),
    path('report/',findMostPopularBooks.as_view(),name="MostPopularBooks"),
    path('report/borrowingsBook',borrowing_book,name='borrowing_book'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='resetpassword/password_reset_form.html'), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name='resetpassword/password_reset_done.html'), name='password_reset_done'),
    path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='resetpassword/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='resetpassword/password_reset_complete.html'), name='password_reset_complete'),

]