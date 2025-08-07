from django.db import models

class author(models.model):
    name = models.CharField(max_length=200)

    def __str__(self)
        return self.name
    

class book(models.model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(author,on_delete=models.CASCADE, related_name='books')