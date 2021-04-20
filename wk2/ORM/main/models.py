from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    # Time/Date Stamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=60)
    num_of_pages = models.IntegerField()
    genre = models.CharField(max_length=20)
    author = models.ForeignKey(Author, related_name = "books", on_delete = models.CASCADE)
    # Time/Date Stamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
