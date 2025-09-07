from django.shortcuts import render, redirect
from .models import Library
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


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