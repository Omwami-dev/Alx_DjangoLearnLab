
## Create
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984>


## retrieve
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# 1984 George Orwell 1949


## update
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# <Book: Nineteen Eighty-Four>


## delete
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# <QuerySet []>


