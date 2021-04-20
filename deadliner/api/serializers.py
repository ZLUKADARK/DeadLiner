from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Task
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title','deadline','completed','importance','id','user',)







