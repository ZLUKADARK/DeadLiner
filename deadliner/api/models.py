from django.db import models
from datetime import timedelta


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    IMPORTANCE = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    )
    importance = models.CharField(max_length=1, choices=IMPORTANCE)
    deadline = models.DateField()
    date_joined = models.DateField(auto_now_add=True)          
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return self.title




    



