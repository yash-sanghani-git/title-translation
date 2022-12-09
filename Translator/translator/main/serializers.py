from rest_framework import serializers
from .models import Profile

class LanguageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile 
        fields = ("id", "title", "language")


class TitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile 
        fields = ("id", "title")