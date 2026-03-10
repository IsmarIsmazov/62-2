from django import forms

from books.models import Category, Tag


class CreateBookForm(forms.Form):
    title = forms.CharField()
    author = forms.CharField()
    description = forms.CharField()
    image = forms.ImageField()
    content = forms.CharField()

    def clean(self):
        data = self.cleaned_data 
        if data.get("title") == data.get("author"):
            raise forms.ValidationError("Title and author must be different")
        return data 

    def clean_title(self):
        data = self.cleaned_data.get("title")
        if data == "title":
            raise forms.ValidationError("Title must be different")
        return data
    
    def clean_author(self):
        data = self.cleaned_data.get("author")
        if data == "author":
            raise forms.ValidationError("Author must be different")
        return data
    

class SearchForm(forms.Form):
    author_choice = [("author1", "Ismar"), ("author2", "Emir")]
    example_choice = [("example1", "Ismar"), ("example2", "Emir")]
    search = forms.CharField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False) # динамичный одиночные выбор
    author = forms.ChoiceField(choices=author_choice, required=False) # статичный одиночные выбор
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False) # динамичный множественный выбор
    example = forms.MultipleChoiceField(choices=author_choice, required=False)
