from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description','is_completed' , 'deadline', 'priority', 'is_completed', 'user']
