from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class BlogEntry(models.Model):
    title=models.CharField(max_length=100)
    BlogPost=models.TextField()
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.title
def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
