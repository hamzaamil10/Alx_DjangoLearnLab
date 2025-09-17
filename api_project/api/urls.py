from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  
    path('api/', include(router.urls)),

]