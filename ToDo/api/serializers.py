from rest_framework import  serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ('title', 'description', 'status_of_task', 'due_date')
