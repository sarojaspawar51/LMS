from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Author, Book, Library, Librarian, BorrowedBook
from .serializers import AuthorSerializer, BookSerializer, LibrarySerializer, LibrarianSerializer, BorrowedBookSerializer, UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import User

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LibraryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class LibraryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class LibrarianListCreateAPIView(generics.ListCreateAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

class LibrarianDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

class BorrowedBookListCreateAPIView(generics.ListCreateAPIView):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer

class BorrowedBookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AuthorAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            # author_objs = get_object_or_404(Author, pk=pk)
            try:
                author_objs = Author.objects.get(id=pk)
                print(f'127-------{author_objs}')
            except Author.DoesNotExist:
                return Response({'status':'fail','message': f'Invaild Id:- {pk}.',}, status=status.HTTP_404_NOT_FOUND)

            serialized_data = AuthorSerializer(author_objs).data
            return Response({'status':'success','message': 'Data Fetch successfully', 'data':serialized_data}, status=status.HTTP_200_OK)
        else:
            author_objs = Author.objects.all()
            print(f'135-------{author_objs}')
            serialized_data = AuthorSerializer(author_objs, many=True).data
            return Response({'status':'success','message': 'Data Fetch successfully', 'data':serialized_data}, status=status.HTTP_200_OK)

    def post(self, request):
            serializer = AuthorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'Author created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
            

class AuthorInfoAPIView(APIView):
      def put(self, request, pk=None):
        if pk is None:
            return Response({'status': 'fail', 'message': 'Must provide ID for updating'}, status=status.HTTP_400_BAD_REQUEST)

        author_obj = get_object_or_404(Author, id=pk)
        serializer = AuthorSerializer(author_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': f'Author with ID {pk} updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

      def patch(self, request, pk=None):
           if pk is None:
                 return Response({'status': 'fail', 'message': 'Must provide ID for partial update'}, status=status.HTTP_400_BAD_REQUEST)
           author_obj = get_object_or_404(Author, id=pk)
           name=request.data.get('name')
           serializer = AuthorSerializer(instance=author_obj, data={'name':name}, partial=True)
           if serializer.is_valid():
                 serializer.save()
                 return Response({'status': 'success', 'message': f'Author with ID {pk} partially updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

      def delete(self, request, pk=None):
            if pk is None:
                  return Response({'status': 'fail', 'message': 'Must provide ID for deletion'}, status=status.HTTP_400_BAD_REQUEST)
            author_obj = get_object_or_404(Author, id=pk)
            author_obj.delete()
            return Response({'status': 'success', 'message': f'Author with ID {pk} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



class BookAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            
            try:
                book_objs = Book.objects.get(id=pk)
                print(f'127-------{book_objs}')
            except Book.DoesNotExist:
                return Response({'status':'fail','message': f'Invaild Id:- {pk}.',}, status=status.HTTP_404_NOT_FOUND)

            serialized_data = BookSerializer(book_objs).data
            return Response({'status':'success','message': 'Data Fetch successfully', 'data':serialized_data}, status=status.HTTP_200_OK)
        else:
            book_objs = Book.objects.all()
            print(f'135-------{book_objs}')
            serialized_data = BookSerializer(book_objs, many=True).data
            return Response({'status':'success','message': 'Data Fetch successfully', 'data':serialized_data}, status=status.HTTP_200_OK)
    
    def post(self, request):
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'message': 'Book created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookInfoAPIView(APIView):
      def put(self, request, pk=None):
        if pk is None:
            return Response({'status': 'fail', 'message': 'Must provide ID for updating'}, status=status.HTTP_400_BAD_REQUEST)

        book_obj = get_object_or_404(Book, id=pk)
        serializer = BookSerializer(book_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': f'Book with ID {pk} updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

      def patch(self, request, pk=None):
           if pk is None:
                 return Response({'status': 'fail', 'message': 'Must provide ID for partial update'}, status=status.HTTP_400_BAD_REQUEST)
           book_obj = get_object_or_404(Book, id=pk)
           title=request.data.get('title')
           serializer = BookSerializer(instance=book_obj, data={'title':title}, partial=True)
           if serializer.is_valid():
                 serializer.save()
                 return Response({'status': 'success', 'message': f'Book with ID {pk} partially updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

      def delete(self, request, pk=None):
            if pk is None:
                  return Response({'status': 'fail', 'message': 'Must provide ID for deletion'}, status=status.HTTP_400_BAD_REQUEST)
            book_obj = get_object_or_404(Book, id=pk)
            book_obj.delete()
            return Response({'status': 'success', 'message': f'Book with ID {pk} deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



