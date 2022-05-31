from datetime import date
from turtle import title
from django.db import models

# Create your models here.
class todo_now(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title