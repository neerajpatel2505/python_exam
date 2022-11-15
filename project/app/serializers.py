from models import UserDatabase
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    fname=serializers.CharField(max_length=100)
    lname=serializers.CharField(max_length=100)
    mobile=serializers.IntegerField()
    email=serializers.EmailField()
    password=serializers.CharField(max_length=100)