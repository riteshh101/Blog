from django.db import models
import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    uname = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now=True)

#model for contact

class contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    desc =models.TextField()

