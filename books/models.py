from django.db import models

# Select * from books;
# Book.objects.all()

# select * from books where title = 'Интесресно';
# Book.objects.filter(title='Интесресно')

# select * from books where id = 1;
# Book.objects.get(id=1)


# update books set title = 'title' where id = 1;
'''
books = Book.objects.filter(name=1)
for i in books:
    i.title = 'title'
    i.save()
'''

# insert into books(title, author, description) values("title", "author", "description");
# Book.objects.create(title='title', author='author', description='description')

# Create your models here.
# ORM - Object Relational Mapping

# OneToMany - один ко многим | одна категория много статьи
# ManyToMany - многие ко многим
# OneToOne - один ко одному

# FK - Foreign Key связь который единственный в базе данных

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to="books")
    description = models.TextField()
    content = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    