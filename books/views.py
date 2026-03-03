from django.http import HttpResponse
from django.shortcuts import redirect, render

from books.models import Book

# Create your views here.


def home(request):
    return render(request, 'home.html')
    
def list_ref_books(request):
    all_books = Book.objects.all()
    return render(request=request, template_name="books/list_books.html", context={"books": all_books})

def detail_book(request, id):
    book = Book.objects.get(id=id)
    return render(request=request, template_name="books/detail_book.html", context={"book": book})

def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        content = request.POST.get("content")

        Book.objects.create(title=title, author=author, description=description, image=image, content=content)
        return redirect(f"/books/")
    elif request.method == "GET":
        return render(request=request, template_name="books/create_book.html")