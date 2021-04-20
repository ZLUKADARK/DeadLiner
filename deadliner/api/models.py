from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=3000)
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




    



