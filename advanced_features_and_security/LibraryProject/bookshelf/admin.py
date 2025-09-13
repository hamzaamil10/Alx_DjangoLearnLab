from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Show these columns in admin list
    list_filter = ("publication_year", "author")            # Add sidebar filters
    search_fields = ("title", "author")                     # Add search bar for these fields

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "date_of_birth", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")

admin.site.register(CustomUser, CustomUserAdmin)