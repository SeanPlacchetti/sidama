from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Sidama, Roaster, Country, Varietal, Quality, Bean, Region, Tag, BeanRegion, BeanVarietal, \
    BeanQuality, BeanTag

__author__ = 'seanplacchetti'


class SidamaSerializer(serializers.HyperlinkedModelSerializer):
    sidama_id = serializers.IntegerField(source='id', read_only=True)
    creation_date = serializers.DateTimeField(source='created_at', read_only=True)
    useragent = serializers.CharField(source='user_agent', read_only=True)
    class Meta:
        model = Sidama
        fields = ('sidama_id', 'creation_date', 'useragent', 'message')


class RoasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roaster
        fields = ('name', 'website', 'city', 'state', 'roaster_id')


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'continent', 'country_id')


class VarietalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Varietal
        fields = ('name', 'varietal_id')


class QualitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quality
        fields = ('quality_id', 'description')


class BeanRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeanRegion


class BeanVarietalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeanVarietal


class BeanQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BeanQuality


class BeanTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeanTag


class BeanSerializer(serializers.HyperlinkedModelSerializer):
    qualities = BeanQualitySerializer(source='bean_quality', many=True)
    regions = BeanRegionSerializer(source='bean_region', many=True)
    tags = BeanTagSerializer(source='bean_tag', many=True)
    varietals = BeanVarietalSerializer(source='bean_varietal', many=True)

    class Meta:
        model = Bean
        fields = ('roaster_id', 'roasted_date', 'bean_id', 'qualities', 'regions', 'tags', 'varietals')


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ('name', 'country_id', 'region_id')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'tag_id')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
