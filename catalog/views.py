from django.shortcuts import render
from django.views import View
from .models import *


class HomeView(View):
    def get(self,request,*args,**kwargs):
        num_books=Book.objects.all().count()
        num_instances=BookInstance.objects.all().count()
        num_instances_available=BookInstance.objects.filter(status__exact='a').count()
        num_authors=Author.objects.count()
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors
        }
        return render(request,'catalog/home.html',context)

class BooksView(View):
    def get(self,request,*args,**kwargs):
        books=Book.objects.all()
        context={"books":books}
        return render(request,'catalog/books.html',context)
    
class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        book_instance=Book.objects.get(id=pk)
        context={"book":book_instance}
        return render(request,'catalog/book.html',context)
    
class AuthorsView(View):
    def get(self,request,*args,**kwargs):
        authors=Author.objects.all()
        context={"authors":authors}
        return render(request,'catalog/authors.html',context)
    
class AuthorDetailView(View):
    def get(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        author_instance=Author.objects.get(id=pk)
        context={"book":author_instance}
        return render(request,'catalog/author.html',context)