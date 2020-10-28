from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    authors = models.ManyToManyField(Author, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
