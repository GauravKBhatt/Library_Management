from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name="Home"),
    # path('home/',HomeView.as_view(),name="Home"),
    path('books/',BookListView.as_view(),name="Books"),
    path('authors/',AuthorListView.as_view(),name="Authors"),
    path('book/<str:pk>',BookDetailView.as_view(),name="book-detail"),
    path('author/<str:pk>',AuthorDetailView.as_view(),name="author-detail"),
    path('mybooks/',LoanedBookInstancesByUserListView.as_view(),name='my-borrowed'),
    path('librarianview/',LibrarianView.as_view(),name='all-borrowed'),
    path('book/<uuid:pk>/renew/',BookRenewLibrarian.as_view(),name='renew-book-librarian'),
    path('author/create/', AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete')
]
