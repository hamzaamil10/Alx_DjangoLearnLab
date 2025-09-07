from django.urls import path
from . import views
from django.views.generic import RedirectView
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView  

urlpatterns = [
   
    path("books/", views.list_books, name="list_books"),
    path("libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register())
]
