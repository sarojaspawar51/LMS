from django.urls import include, path
from .views import  AuthorAPIView, AuthorInfoAPIView, AuthorListCreateAPIView, AuthorDetailAPIView, BookAPIView, BookInfoAPIView, BookListCreateAPIView, BookDetailAPIView, LibraryListCreateAPIView, LibraryDetailAPIView, LibrarianListCreateAPIView, LibrarianDetailAPIView, BorrowedBookListCreateAPIView, BorrowedBookDetailAPIView, UserDetailAPIView, UserListCreateAPIView


urlpatterns = [
    
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('libraries/', LibraryListCreateAPIView.as_view(), name='library-list-create'),
    path('libraries/<int:pk>/', LibraryDetailAPIView.as_view(), name='library-detail'),
    path('librarians/', LibrarianListCreateAPIView.as_view(), name='librarian-list-create'),
    path('librarians/<int:pk>/', LibrarianDetailAPIView.as_view(), name='librarian-detail'),
    path('borrowed-books/', BorrowedBookListCreateAPIView.as_view(), name='borrowed-book-list-create'),
    path('borrowed-books/<int:pk>/', BorrowedBookDetailAPIView.as_view(), name='borrowed-book-detail'),
     path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    
    path('get/authors/', AuthorAPIView.as_view()),
    path('get/authors/<int:pk>', AuthorAPIView.as_view()),
    path('get/authors/<int:pk>/', AuthorInfoAPIView.as_view()),
    path('get/books/', BookAPIView.as_view()),
    path('get/books/<int:pk>', BookAPIView.as_view()),
    path('get/books/<int:pk>/', BookInfoAPIView.as_view()),
    path('auth/', include('rest_framework.urls'))
    
]
