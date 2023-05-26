from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .permission import IsNoteOwner, IsStickyNoteOwner

# Create your views here.
class StickyNoteViewSet(ModelViewSet):
    queryset = StickyNote.objects.all()
    serializer_class = StickyNoteSerializer
    permission_class = [IsStickyNoteOwner] # we are adding a base permission to make sure only the creator of the note accesses it and perform changes but with this buildIn class another user can update your note if the add thier id

    # This creates a sticky note linked to the user 
    def create(self, request):
        data = request.data
        data['creator'] = request.user.id # we added the forign key to the data before sending the data it to the database
        serializer = self.get_serializer(data=data) # we serialize the data and check if its valide before storing it
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer) #  now we create the data in the database
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # This updates the sticky notes linked to a user
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object() # here we create an instance of our object
        data = request.data # we get the data inorder to added the editor field into it
        data['editor'] = request.user.id  # we add our forign key to the data before storing it
        serializer = self.get_serializer(instance, data=data, partial=partial) # we validate the serializer before we then perform updates 
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer) 

        # we return a concised response
        return Response(serializer.data)
    
    #  This function deletes the notes and returns data
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"message" : "Record was deleted"}, status=status.HTTP_204_NO_CONTENT)

    # This makes sure that data for a specific user
    def get_queryset(self):
        return super().get_queryset().filter(editor=self.request.user)


#  This represent our Note API to be consumed
"""
    We are to make sure the user can create, update , read and delete based on the user data 
"""
class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_class = [IsNoteOwner] # This is a personal customised permission to allow only users accesss ther data

    # This creates a note linked to the user 
    def create(self, request):
        data = request.data
        data['editor'] = request.user.id # we added the forign key to the data before sending it to the database
        serializer = self.get_serializer(data=data) # we serialize the data and check if its valide before storing it
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer) #  now we create the data in the database
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # This updates the notes linked to a user
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object() # here we create an instance of our object
        data = request.data # we get the data inorder to added the editor field into it
        data['editor'] = request.user.id  # we add our forign key to the data before storing it
        serializer = self.get_serializer(instance, data=data, partial=partial)
        
        # we validate the serializer before we then perform updates 
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer) 

        # we return a concised response
        return Response(serializer.data)

    #  This function deletes the notes and returns data
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({"message" : "Record was deleted"}, status=status.HTTP_204_NO_CONTENT)

    # This makes sure that data for a specific user
    def get_queryset(self):
        return super().get_queryset().filter(editor=self.request.user)
    