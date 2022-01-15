from django.contrib import admin

from .models import Book, Author,Address,Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ("rating","author")
    list_display = ("title","author", "get_book_author_first_name", "get_book_author_last_name",)

    
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)