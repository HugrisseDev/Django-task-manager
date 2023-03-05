from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    date_posted = models.TimeField(auto_now=True, null=True)