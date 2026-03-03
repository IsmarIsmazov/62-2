"""
URL configuration for ref_book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path

from books.views import create_book, detail_book, home, list_ref_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("books/", list_ref_books),
    path("books/<int:id>/", detail_book),
    path("books/create/", create_book)
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
