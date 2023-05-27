from django.db import models
from django.contrib.auth.models import User

"""
    Django rest framework has a default User that contain almost all the attributes we need for our design
"""
    

class StickyNote(models.Model):
    content = models.CharField(max_length=300)
    color = models.CharField(max_length=30)
    favorite = models.BooleanField()
    label = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE) # we take our foreign from the base user

    def __str__(self):
        return self.content
    

class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    tag = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    editor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

