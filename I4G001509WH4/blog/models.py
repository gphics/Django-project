from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(user, on_delete=models.CASCADE)
    Created_date=models.DateTimeField()
    Published_date = models.DateTimeField()
   
    