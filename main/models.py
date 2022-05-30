import email
from email import message
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()