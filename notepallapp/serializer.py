from rest_framework import serializers
from .models import  StickyNote, Note
from django.contrib.auth.models import User

# Person serializer
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class StickyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickyNote
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
    
    