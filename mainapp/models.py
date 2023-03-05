from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    date_posted = models.TimeField(auto_now=True, null=True)
    
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        
        return self.title