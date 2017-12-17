from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import Sidama, Roaster, Country, Varietal, Quality, Bean, Region, Tag
from .serializers import SidamaSerializer, UserSerializer,\
    RoasterSerializer, CountrySerializer, VarietalSerializer,\
    QualitySerializer, BeanSerializer, RegionSerializer, TagSerializer

__author__ = 'seanplacchetti'


# ViewSets define the view behavior.
class SidamaViewSet(viewsets.ModelViewSet):
    queryset = Sidama.objects.all()
    serializer_class = SidamaSerializer

    def perform_create(self, serializer):
        serializer.save()


class RoasterViewSet(viewsets.ModelViewSet):
    queryset = Roaster.objects.all()
    serializer_class = RoasterSerializer

    def perform_create(self, serializer):
        serializer.save()


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def perform_create(self, serializer):
        serializer.save()


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def perform_create(self, serializer):
        serializer.save()


class VarietalViewSet(viewsets.ModelViewSet):
    queryset = Varietal.objects.all()
    serializer_class = VarietalSerializer

    def perform_create(self, serializer):
        serializer.save()


class QualityViewSet(viewsets.ModelViewSet):
    queryset = Quality.objects.all()
    serializer_class = QualitySerializer

    def perform_create(self, serializer):
        serializer.save()


class BeanViewSet(viewsets.ModelViewSet):
    queryset = Bean.objects.all()
    serializer_class = BeanSerializer

    def perform_create(self, serializer):
        serializer.save()


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        serializer.save()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
