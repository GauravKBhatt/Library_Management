import datetime
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *
from django.views.generic import ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from catalog.forms import RenewBookForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib import messages

class HomeView(LoginRequiredMixin,View):
    login_url='/login/'
    redirect_field_name='redirect_to'
    def get(self,request,*args,**kwargs):
        num_books=Book.objects.all().count()
        num_instances=BookInstance.objects.all().count()
        num_instances_available=BookInstance.objects.filter(status__exact='a').count()
        num_authors=Author.objects.count()
        num_visits=request.session.get('num_visits',0)
        num_visits+=1
        request.session['num_visits']=num_visits
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
            'num_visits':num_visits
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
    
class AuthorListView(ListView):
    model=Author
    template_name="catalog/authors.html"
    context_object_name="authors"
    paginate_by=5    
class AuthorDetailView(DetailView):
    model=Author
    template_name="catalog/author.html"
    context_object_name="author"

class LoanedBookInstancesByUserListView(LoginRequiredMixin,ListView):
    model=BookInstance
    template_name='catalog/bookinstance_list_borrowed_user.html'
    paginate_by=5
    context_object_name="bookinstance_list"

    def get_queryset(self):
        return(
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact='o').order_by('due_back')
        )

class LibrarianView(PermissionRequiredMixin,ListView):
    model=BookInstance
    permission_required='catalog.can_mark_returned'
    template_name='catalog/bookinstance_list_books_librarian.html'
    paginate_by=5

    def get_queryset(self):
        return(
            BookInstance.objects
            .filter(status__exact='o').order_by('due_back')
        )

class BookRenewLibrarian(PermissionRequiredMixin,View):
    permission_required='catalog.can_mark_returned'
    def post(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        book_instance=get_object_or_404(BookInstance,pk=pk)
        form=RenewBookForm(request.POST)
        if form.is_valid():
            book_instance.due_back=form.cleaned_data['renewal_date']
            book_instance.save()
            return HttpResponseRedirect(reverse('all-borrowed'))
    
    def get(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        book_instance=get_object_or_404(BookInstance,pk=pk)
        proposed_renewal_date=datetime.date.today()+datetime.timedelta(weeks=3)
        form=RenewBookForm(initial={'renewal_date':proposed_renewal_date})
        context={
            'form':form,
            'book_instance':book_instance}
        return render(request,'catalog/book_renew_librarian.html',context)

class AuthorCreate(PermissionRequiredMixin,CreateView):
    model=Author
    fields='__all__'
    initial={'date_of_death':'11/11/2024'}
    permission_required='catalog.add_author'

class AuthorUpdate(PermissionRequiredMixin,UpdateView):
    model=Author
    fields='__all__'
    permission_required='catalog.change_author'

class AuthorDelete(PermissionRequiredMixin,DeleteView):
    model=Author
    success_url=reverse_lazy('Authors')
    permission_required='catalog.delete_author'

    def form_valid(self,form):
        pk=self.object.pk
        try:
            self.object.delete()
            messages.success(self.request,"Author deleted successfully.")
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            messages.error(self.request,f"Error deleting author:{e}")
            return HttpResponseRedirect(self.success_url)
