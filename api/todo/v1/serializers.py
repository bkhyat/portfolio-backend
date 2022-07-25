from datetime import datetime

from rest_framework import serializers

from todo.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

    def update(self, instance, validated_data):
        completed_at = None
        if self.instance.is_completed ^ self.validated_data.get('is_completed', False):
            if not self.instance.is_completed:
                completed_at = datetime.now()
        for key,val in validated_data.items():
            setattr(instance, key, val)
        instance.completed_at = completed_at
        instance.save()
        return instance
