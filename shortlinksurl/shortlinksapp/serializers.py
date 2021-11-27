from rest_framework import serializers
from .models import shortlinksapp

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = shortlinksapp 
        fields = ['shortId', 'OriginalUrl', 'ShortUrl']