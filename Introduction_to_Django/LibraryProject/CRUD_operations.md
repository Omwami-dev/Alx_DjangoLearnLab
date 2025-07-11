
## Create
from bookshelf.models import Book
book = Book.objects.create(title=
1984, author=George
Orwell, publication_year=1949)
book

## retrieve
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

## update
book.title = "Nineteen Eighty-Four"
book.save()
book

## delete
book.delete()
Book.objects.all()


