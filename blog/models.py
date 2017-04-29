from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class BlogEntry(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateTimeField()
    
    def __str__(self):
     return self.title