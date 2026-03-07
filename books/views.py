import re

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from books.forms import CreateBookForm
from books.models import Book
from users.forms import SignUpForm

# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    
def list_ref_books(request):
    if request.method == "GET":
        all_books = Book.objects.all()
        return render(request=request, template_name="books/list_books.html", context={"books": all_books})

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
    