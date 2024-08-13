from rest_framework import serializers
from .models import Author, Book, Library, Librarian, BorrowedBook, User

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class LibrarySerializer(serializers.ModelSerializer):
    librarians = serializers.StringRelatedField(many=True, read_only=True)
    librarians_id = serializers.PrimaryKeyRelatedField(queryset=Librarian.objects.all(), many=True, write_only=True, source='librarians')

    class Meta:
        model = Library
        fields = ['id', 'name', 'address', 'librarians','librarians_id']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    libraries = LibrarySerializer(many=True, read_only=True)
    authors_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True, write_only=True, source='authors')
    libraries_id = serializers.PrimaryKeyRelatedField(queryset=Library.objects.all(), many=True, write_only=True, source='libraries')
    class Meta:
        model = Book
        fields = ['id', 'title', 'authors', 'libraries','authors_id','libraries_id']


class LibrarianSerializer(serializers.ModelSerializer):
   
    # library_name = serializers.CharField(source='library.name', read_only=True)

    class Meta:
        model = Librarian
        fields = ['id', 'name']

    
class BorrowedBookSerializer(serializers.ModelSerializer):
    book_name = serializers.CharField(source='book.title', read_only=True)
    user_name = serializers.CharField(source='user.name', read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = BorrowedBook
        fields = ['id', 'book',  'book_name', 'user','user_name', 'borrowed_date', 'due_date']
       
class UserSerializer(serializers.ModelSerializer):
    books_borrowed=BookSerializer(many=True, read_only=True)
    books_borrowed_ids=serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(),many=True,write_only=True,source='books_borrowed')

    class Meta:
        model = User
        fields = ['id', 'name','books_borrowed','books_borrowed_ids']
