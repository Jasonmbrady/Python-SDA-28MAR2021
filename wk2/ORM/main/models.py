from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=60)
    num_of_pages = models.IntegerField()
    release_date = models.DateTimeField()
    author = models.CharField(max_length=60)
    # Time/Date Stamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)