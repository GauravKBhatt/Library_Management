from django.shortcuts import render
from django.views import View
from .models import *
from django.views.generic import ListView,DetailView


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

class BookListView(ListView):
    model=Book
    template_name='catalog/books.html'
    context_object_name='books'
    paginate_by=2
    # def get(self,request,*args,**kwargs):
    #     books=Book.objects.all()
    #     context={"books":books}
    #     return render(request,'catalog/books.html',context)
    
class BookDetailView(ListView):
    def get(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        book_instance=Book.objects.get(id=pk)
        context={"book":book_instance}
        return render(request,'catalog/book.html',context)
    
class AuthorsView(ListView):
    model=Author
    template_name="catalog/authors.html"
    context_object_name="authors"
    paginate_by=5    
class AuthorDetailView(DetailView):
    model=Author
    template_name="catalog/author.html"
    context_object_name="author"