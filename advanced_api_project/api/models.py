from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name


class book(models.Model):
    tittle = models.CharField()
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        return self.title

