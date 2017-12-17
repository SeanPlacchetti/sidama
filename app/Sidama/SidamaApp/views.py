from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import Sidama
from .serializers import SidamaSerializer, UserSerializer

__author__ = 'seanplacchetti'


# ViewSets define the view behavior.
class SidamaViewSet(viewsets.ModelViewSet):
    queryset = Sidama.objects.all()
    serializer_class = SidamaSerializer

    def perform_create(self, serializer):
        serializer.save(user_agent=self.request.META['HTTP_USER_AGENT'])


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
