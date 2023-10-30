from rest_framework import serializers
from models import Album


class AlbumSerializer(serializers.Serializer):
    class Meta:
        model = Album
        fields = ['user', 'is_public', 'name']
