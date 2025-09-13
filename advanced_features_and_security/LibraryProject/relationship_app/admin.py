from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(Book)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

