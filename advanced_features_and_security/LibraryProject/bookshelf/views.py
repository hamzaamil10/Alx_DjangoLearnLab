from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.views.decorators.http import require_http_methods
from .models import Book
from django.db.models import Q
from .forms import ExampleForm


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]


def book_list(request):
    books = Book.objects.select_related("author").all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# --- CREATE ---
@permission_required("relationship_app.can_create", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/book_form.html", {"form": form, "mode": "add"})

# --- EDIT/UPDATE ---
@permission_required("relationship_app.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/book_form.html", {"form": form, "mode": "edit", "book": book})

# --- DELETE ---
@permission_required("relationship_app.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/book_confirm_delete.html", {"book": book})

@require_http_methods(["GET"])
def book_list(request):
    """
    Safe search: validated by BookSearchForm, ORM uses parameters to prevent SQLi.
    """
    form = BookSearchForm(request.GET or None)
    qs = Book.objects.select_related("author").all()

    if form.is_valid():
        q = form.cleaned_data["q"]
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(author__name__icontains=q))

    return render(request, "bookshelf/book_list.html", {"books": qs, "form": form})


@require_http_methods(["GET", "POST"])
def create_book(request):
    """
    Example POST view: CSRF protected by CsrfViewMiddleware + template {% csrf_token %}.
    Uses ModelForm (not shown) to validate/sanitize inputs.
    """
    from .forms import BookForm  # assume you have one
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})
