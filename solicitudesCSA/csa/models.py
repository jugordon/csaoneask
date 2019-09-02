"""
Definition of models.
"""

from django.db import models
from django.contrib import admin

# Create your models here.


class workRequest(models.Model):
    alias_requester = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)