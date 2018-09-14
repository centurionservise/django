from django.db import models

# Create your models here.

class Articles(models.Model):
    title=models.CharField(max_len=125)
    post=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.title
        