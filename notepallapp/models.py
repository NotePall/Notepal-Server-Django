from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    

class StickyNote(models.Model):
    content = models.CharField(max_length=300)
    color = models.CharField(max_length=10)
    favorite = models.BooleanField()
    label = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    

class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    tag = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    editor = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

