from rest_framework import serializers
from django.contrib.auth.models import User

# we created our serializer to handle the project
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    