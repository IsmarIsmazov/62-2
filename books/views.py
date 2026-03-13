
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from books.forms import CreateBookForm, SearchForm
from books.models import Book

# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    
def list_ref_books(request):
    if request.method == "GET":
        all_books = Book.objects.all()
        limit = 3
        page = int(request.GET.get("page", 1)) 
        max_page = all_books.count() // limit + 1
        list_pages = range(1, max_page + 1)
        start = (page - 1) * limit
        end = page * limit
        all_books = all_books[start:end]
        form = SearchForm(request.GET)
        if not form.is_valid():
            return HttpResponse("Не существующий параметр")
        search = form.cleaned_data.get("search", None)
        category = form.cleaned_data.get("category", None)
        author = form.cleaned_data.get("author", None)
        tags = form.cleaned_data.get("tags", None)
        if search:
            all_books = all_books.filter(Q(title__icontains=search) | Q(description__icontains=search))
        if category:
            all_books = all_books.filter(category=category)
        if author:
            print(author)
        if tags:
            all_books = all_books.filter(tags__in=tags)
        return render(
            request=request, 
            template_name="books/list_books.html", 
            context={"books": all_books, "form": form, "list_pages": list_pages}
            )

def detail_book(request, id):
    if request.method == "GET":
        book = Book.objects.get(id=id)
        return render(request=request, template_name="books/detail_book.html", context={"book": book})

@login_required(login_url="/users/sign-in/")
def create_book(request):
    if request.method == "POST":
        form = CreateBookForm(request.POST, request.FILES)
        if not form.is_valid():
            return HttpResponse("Error data")
        title = form.cleaned_data.get("title")
        author = form.cleaned_data.get("author")
        description = form.cleaned_data.get("description")
        image = form.cleaned_data.get("image")
        content = form.cleaned_data.get("content")
        Book.objects.create(title=title, author=author, description=description, image=image, content=content)
        return redirect(f"/books/")
    elif request.method == "GET":
        form = CreateBookForm()
        return render(request=request, template_name="books/create_book.html", context={"form": form})
    