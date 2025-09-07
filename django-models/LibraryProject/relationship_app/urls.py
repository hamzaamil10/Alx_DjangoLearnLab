from django.urls import path
from . import views
from django.views.generic import RedirectView
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView  

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="login", permanent=False)),

    path("books/", views.list_books, name="list_books"),
    path("libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

    path("roles/admin/", views.admin_view, name="admin_view"),
    path("roles/librarian/", views.librarian_view, name="librarian_view"),
    path("roles/member/", views.member_view, name="member_view"),

    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
]
