__author__ = 'seanplacchetti'
from django.db import models


class Sidama(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=400, blank=True)
    message = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return "(Sidama: " + self.message + ")"
