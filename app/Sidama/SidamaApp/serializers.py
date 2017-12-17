from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Sidama

__author__ = 'seanplacchetti'


class SidamaSerializer(serializers.HyperlinkedModelSerializer):
    sidama_id = serializers.IntegerField(source='id', read_only=True)
    creation_date = serializers.DateTimeField(source='created_at', read_only=True)
    useragent = serializers.CharField(source='user_agent', read_only=True)
    class Meta:
        model = Sidama
        fields = ('sidama_id', 'creation_date', 'useragent', 'message' )


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
