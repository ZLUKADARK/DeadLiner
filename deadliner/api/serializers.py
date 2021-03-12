from rest_framework import serializers
from datetime import timedelta, datetime
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title','deadline','completed')






