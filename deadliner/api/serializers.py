from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title','description', 'deadline', 'date_joined', 'completed', 'objects',)

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title','deadline','completed')