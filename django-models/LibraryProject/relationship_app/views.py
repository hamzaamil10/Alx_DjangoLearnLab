from django.shortcuts import render, redirect
from .models import Library
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test


def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = "library"
    template_name = "relationship_app/library_detail.html"


def register(request):
    """Simple user registration using Django's built-in UserCreationForm."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("list_books")  
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


def _has_role(user, role_name: str) -> bool:
    return (
        user.is_authenticated
        and hasattr(user, "profile")
        and user.profile.role == role_name
    )

def is_admin(user):     return _has_role(user, "Admin")
def is_librarian(user): return _has_role(user, "Librarian")
def is_member(user):    return _has_role(user, "Member")

@user_passes_test(is_admin, login_url="login")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian, login_url="login")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member, login_url="login")
def member_view(request):
    return render(request, "relationship_app/member_view.html")