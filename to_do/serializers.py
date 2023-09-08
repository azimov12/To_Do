from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['task_name', 'created_at', 'updated_at', 'status', 'desc']