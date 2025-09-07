from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def list_books(request):
    books = Book.objects.select_related("author").all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    context_object_name = "library"
    template_name = "relationship_app/library_detail.html"


class RegisterView(View):
    template_name = "relationship_app/register.html"

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in immediately after successful registration
            auth_login(request, user)
            # Redirect wherever makes sense in your app
            return redirect("list_books")  # change if you prefer a different landing page
        return render(request, self.template_name, {"form": form})
