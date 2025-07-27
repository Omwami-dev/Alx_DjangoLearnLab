# bookshelf/forms.py

from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    A secure example form using Django's built-in form system
    to prevent SQL injection, XSS, and handle user input validation.
    """
    class Meta:
        model = Book
        fields = ['title', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

    def clean_author(self):
        author = self.cleaned_data['author'].strip()
        if not author:
            raise forms.ValidationError("Author field cannot be empty.")
        return author
