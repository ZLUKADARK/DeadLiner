from django.db import models
from datetime import timedelta, datetime


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    deadline = models.DateField()
    date_joined = models.DateField(auto_now_add=True)
    time_left = models.timedelta()   
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return self.title

