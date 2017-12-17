__author__ = 'seanplacchetti'
from django.db import models


class Sidama(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=400, blank=True)
    message = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return "(Sidama: " + self.message + ")"


class Bean(models.Model):
    roaster_id = models.ForeignKey('Roaster', on_delete=models.CASCADE)
    roasted_date = models.DateTimeField(auto_now_add=False)
    bean_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return "(Bean: " + self.id + ")"


class Roaster(models.Model):
    name = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    roaster_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return "(Roaster: " + self.name + ")"


class Country(models.Model):
    name = models.CharField(max_length=100, blank=True)
    continent = models.CharField(max_length=400, blank=True)
    country_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return "(Country: " + self.name + ")"


class Region(models.Model):
    name = models.CharField(max_length=100, blank=True)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE)
    region_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return "(Region: " + self.name + ")"


class Varietal(models.Model):
    name = models.CharField(max_length=100, blank=True)
    varietal_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return "(Varietal: " + self.name + ")"


class Quality(models.Model):
    description = models.CharField(max_length=50, blank=True)
    quality_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return "(Quality: " + self.description + ")"


class Tag(models.Model):
    name = models.CharField(max_length=50, blank=True)
    tag_id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return "(Tag: " + self.name + ")"


class BeanRegion(models.Model):
    bean_id = models.ForeignKey('Bean', on_delete=models.CASCADE)
    region_id = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __unicode__(self):
        return "(BeanRegion: " + self.id + ")"


class BeanVarietal(models.Model):
    bean_id = models.ForeignKey('Bean', on_delete=models.CASCADE)
    varietal_id = models.ForeignKey('Varietal', on_delete=models.CASCADE)

    def __unicode__(self):
        return "(BeanVarietal: " + self.id + ")"


class BeanQuality(models.Model):
    bean_id = models.ForeignKey('Bean', on_delete=models.CASCADE)
    quality_id = models.ForeignKey('Quality', on_delete=models.CASCADE)

    def __unicode__(self):
        return "(BeanQuality: " + self.id + ")"


class BeanTag(models.Model):
    bean_id = models.ForeignKey('Bean', on_delete=models.CASCADE)
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE)

    def __unicode__(self):
        return "(BeanTags: " + self.id + ")"