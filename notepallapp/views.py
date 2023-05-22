from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class PersonVieSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class StickyNoteViewSet(ModelViewSet):
    queryset = StickyNote.objects.all()
    serializer_class = StickyNoteSerializer

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
