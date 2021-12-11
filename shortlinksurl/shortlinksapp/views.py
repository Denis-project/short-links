from django.shortcuts import render, redirect 
from .models import shortlinksapp
from rest_framework import generics
from .serializers import shortlinksappSerializer



class ShortlinksappCreate(generics.CreateAPIView):
    queryset = shortlinksapp.objects.all(),
    serializer_class = shortlinksappSerializer
    


# class ShortlinksappList(generics.ListAPIView):
#     queryset = shortlinksapp.objects.all()
#     serializer_class = shortlinksappSerializer
    

# class ShortlinksappDetail(generics.RetrieveAPIView):
#     queryset = shortlinksapp.objects.all()
#     serializer_class = shortlinksappSerializer


class ShortlinksappUpdate(generics.RetrieveUpdateAPIView):
    queryset = shortlinksapp.objects.all()
    serializer_class = shortlinksappSerializer


# class ShortlinksappDelete(generics.RetrieveDestroyAPIView):
#     queryset = shortlinksapp.objects.all()
#     serializer_class = shortlinksappSerializer



