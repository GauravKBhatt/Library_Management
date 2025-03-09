from django.contrib import admin
from .models import *

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

class BookInline(admin.TabularInline):
    model = Book
    extra = 0
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # since genre field is many to many field, to reduce large database access "cost", we use display_genre function.
    list_display=('title','language','author','display_genre')
    inlines = [BooksInstanceInline]

    def display_genre(self):
        return ','.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description='Genre'


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('id','due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # before writing the list display the admin pannel was using the string generated from the model __str__() method.
    list_display=('last_name','first_name','date_of_birth','date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines=[BookInline]

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)
