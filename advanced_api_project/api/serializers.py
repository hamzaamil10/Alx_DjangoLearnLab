from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)
    class Meta:
        model = Author
        fields = ['name']

class BookSerialize(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
