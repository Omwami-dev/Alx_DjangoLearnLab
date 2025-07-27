from django.shortcuts import render
# bookshelf/views.py

from django.contrib.auth import get_user_model
User = get_user_model()

def user_books(request):
    books = Book.objects.filter(user=request.user)
    ...



