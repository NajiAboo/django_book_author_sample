from django.shortcuts import render
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-title")
    num_books = books.count()
    avg_rating =  books.aggregate(Avg("rating"))
    return render(request, 'book_outlet/index.html', {
        "books" : books,
        "total_books":num_books,
        "avg_rating": avg_rating
    })

def book_details(request,id):
    try:
        book = Book.objects.get(pk=id)
    except:
        raise Http404()
    
    return render(request, 'book_outlet/book_detail.html', {"book": book})
    