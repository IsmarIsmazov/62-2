from django import forms


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