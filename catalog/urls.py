from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name="Home"),
    # path('home/',HomeView.as_view(),name="Home"),
    path('books/',BooksView.as_view(),name="Books"),
    path('authors/',AuthorsView.as_view(),name="Authors"),
    path('book/<str:pk>',BookDetailView.as_view(),name="book-detail"),
    path('author/<str:pk>',AuthorDetailView.as_view(),name="author-detail"),
]
