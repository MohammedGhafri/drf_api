from django.shortcuts import render
from rest_framework import generics

from .models import Blog
from .serializer import BlogSerializer

class BlogsList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
