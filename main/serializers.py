from rest_framework import serializers
from .models import Task



class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'body', 'date', 'time',)
        model = Task