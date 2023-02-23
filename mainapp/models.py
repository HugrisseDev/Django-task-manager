from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    review_title = models.CharField(max_length=50)
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.reviewer_name
    