from django.urls import path
from .views import *

urlpatterns=[
    path('',GetRoutes.as_view()),
    path('books/',GetBooks.as_view()),
    path('book/<int:pk>/',GetBook.as_view()),
    path('authors/',GetAuthors.as_view()),
    path('author/<int:pk>/',GetAuthor.as_view()),
]