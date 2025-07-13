from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields shown in list view
    list_filter = ('publication_year', 'author')            # Filters in sidebar
    search_fields = ('title', 'author')                     # Search box

