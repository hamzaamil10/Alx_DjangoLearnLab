from rest_framework import serializers
from .models import Author, Book
import datetime

# BookSerializer: serializes all Book fields, with validation on year.
class BookSerialize(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
# AuthorSerializer: serializes author name and nested books list.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerialize(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books']

