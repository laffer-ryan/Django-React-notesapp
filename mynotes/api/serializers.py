from rest_framework.serializers import ModelSerializer
from django.db import models
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


