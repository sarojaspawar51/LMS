from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    libraries = models.ManyToManyField('Library', related_name='books')

    def __str__(self):
        return self.title
    
    
class Library(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name
    


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    books_borrowed=models.ManyToManyField(Book,related_name="users")

    def __str__(self):
        return self.name   

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)  
    borrowed_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f'{self.book.title} borrowed by {self.user.name}'


