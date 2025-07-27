# bookshelf/forms.py

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

        # Optional: Add HTML input attributes or widgets
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
        }

    # Optional: Add custom validation
    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if len(title) < 3:
            raise forms.ValidationError("Title is too short.")
        return title
