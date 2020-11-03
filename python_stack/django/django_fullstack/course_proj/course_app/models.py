from __future__ import unicode_literals
from django.db import models

## MANAGERS

class Desc_Manager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['content']) < 15:
            errors['content'] = "Description should be at least two characters"
        return errors

class Course_Manager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Name should be at least five characters"
        return errors

## NORMAL

class Description(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Desc_Manager()

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Course_Manager()

class Comment(models.Model):
    content = models.TextField(max_length=500)
    course = models.ForeignKey(Course, related_name= "comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)