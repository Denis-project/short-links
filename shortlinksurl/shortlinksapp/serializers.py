import requests
import pyshorteners
from rest_framework import serializers
from .models import Shortlinksapp

# class ShortlinksappSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = shortlinksapp 
#         fields = ['shortId', 'OriginalUrl', 'ShortUrl']
        
        
class ShortlinksappSerializer(serializers.Serializer):
    shortId = serializers.AutoField(primary_key=True)
    originalUrl = serializers.CharField(max_length=1500)
    shortUrl = serializers.CharField(max_length=500)

    def create(self, validated_data):
        
        return Shortlinksapp.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        instance.originalUrl('originalUrl', instance.originalUrl)
        instance.shortUrl('shortUrl', instance.shortUrl)
        instance.save()
        return instance