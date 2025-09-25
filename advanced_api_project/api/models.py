from django.db import models


# Author model represents a book writer, with one-to-many relation to Book.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Book model includes title, publication year, and FK to Author.
class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, name='book_author')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    


