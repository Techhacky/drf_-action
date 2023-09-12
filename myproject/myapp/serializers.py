
from rest_framework import serializers
from .models import Task

class TaskdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title','description']

class TaskprioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name','priority']
    
class task_priority_data(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['title','description','name','priority']