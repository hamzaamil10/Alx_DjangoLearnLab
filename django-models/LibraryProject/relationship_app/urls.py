from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, list_books, LibraryDetailView 

app_name = "relationship_app"
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("login/",  LoginView.as_view(template_name="relationship_app/login.html"),  name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", RegisterView.as_view(template_name="relationship_app/register.html"), name="register"),    

]