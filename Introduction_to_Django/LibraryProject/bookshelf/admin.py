from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Show these columns in admin list
    list_filter = ("publication_year", "author")            # Add sidebar filters
    search_fields = ("title", "author")                     # Add search bar for these fields

