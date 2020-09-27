from rest_framework import serializers

from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'body', 'created_at','updated_at')
        model = Blog