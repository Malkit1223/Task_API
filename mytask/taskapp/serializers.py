from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
    def validate(self,data):
      # Checks whether the title is in the data then tries to validate 
      if 'title' in data:
            if len(data['title']) < 3:
                raise serializers.ValidationError('Title must be at least 3 characters long.')
            
            if not data['title']:
                raise serializers.ValidationError("Title should not be empty")

        
      if 'description' in data:
            if len(data['description']) < 10:
                raise serializers.ValidationError('Description must be at least 10 characters long.')
            if len(data['description']) > 200:
                raise serializers.ValidationError('Max limit reached')
            
      return data