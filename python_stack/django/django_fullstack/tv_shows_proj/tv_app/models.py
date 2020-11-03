from __future__ import unicode_literals
from django.db import models
from datetime import date

class TV_Manager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least two characters"
        duplicate_test = Show.objects.filter(title = postData['title'])
        if duplicate_test:
            errors['title_duplicate'] = "Title already exists"
        if len(postData['desc']) > 0:
            if len(postData['desc']) < 10:
                errors['desc'] = "Description should be at least ten characters if you choose to add one"
            else:
                pass
        if date(postData['release_date']) > date.today():
            errors['release_date'] = "Date must be in the past"
        return errors

class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(blank=True)
    network = models.ForeignKey(Network, related_name = 'shows', on_delete = models.CASCADE)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TV_Manager()
