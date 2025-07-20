
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by an author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = objects.filter(author=author)
        print(f"Books by {author.name}: {[book.title for book in books]}")
    except Author.DoesNotExist:
        print("Author not found.")

# List all books in a specific library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = Librarian.objects.get(library = )
        print(f"Books in {library.name}: {[book.title for book in books]}")
    except Library.DoesNotExist:
        print("Library not found.")


def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library = )
        print(f"Librarian of {library.name}: {librarian.name}")
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        print("Library or Librarian not found.")

