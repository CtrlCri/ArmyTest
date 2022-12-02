from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'subject', 'description', 'completed')
        read_only_fields = ('completed',)
        