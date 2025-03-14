from rest_framework.views import APIView
from rest_framework.response import Response
from catalog.models import Book,Author
from .serializers import *

class GetRoutes(APIView):
    def get(self,request,*args,**kwargs):
        routes=[
            'GET /api',
            'GET /api/books',
            'GET /api/book/:id',
            'GET /api/authors',
            'GET /api/author/:id'
        ]
        return Response(routes)
    
class GetBooks(APIView):
    def get(self, request, *args, **kwargs):
        books=Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    
class GetBook(APIView):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        book=Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
class GetAuthors(APIView):
    def get(self, request, *args, **kwargs):
        authors=Author.objects.all()
        serializer = AuthorSerializer(authors,many=True)
        return Response(serializer.data)
    
class GetAuthor(APIView):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        author=Author.objects.get(id=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)