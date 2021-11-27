from django.shortcuts import render
from .models import shortlinksapp
from rest_framework import generics
from .serializers import shortlinksappSerializer


class shortlinksappCreate(generics.CreateAPIView):
    queryset = shortlinksapp.objects.all(),
    serializer_class = shortlinksappSerializer


class shortlinksappList(generics.ListAPIView):
    queryset = shortlinksapp.objects.all()
    serializer_class = shortlinksappSerializer
    

class shortlinksappDetail(generics.RetrieveAPIView):
    queryset = shortlinksapp.objects.all()
    serializer_class = shortlinksappSerializer


class shortlinksappUpdate(generics.RetrieveUpdateAPIView):
    queryset = shortlinksapp.objects.all()
    serializer_class = shortlinksappSerializer


class shortlinksappDelete(generics.RetrieveDestroyAPIView):
    queryset = shortlinksapp.objects.all()
    serializer_class = shortlinksappSerializer