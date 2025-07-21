from django.shortcuts import render
from .models import Book
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'relationship_app/register.html', {'form': form})

# A Function for list of all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library

# Class that displays details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .utils import is_admin

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .utils import is_librarian

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .utils import is_member

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')


