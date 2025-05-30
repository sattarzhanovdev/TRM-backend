from rest_framework import serializers
from .models import Worker, Client
from datetime import datetime


def is_string(value):
    return isinstance(value, str)


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
