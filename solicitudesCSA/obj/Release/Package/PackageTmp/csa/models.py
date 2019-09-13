"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from  django.utils import timezone

# Create your models here.

JOB_TITLE_CHOICES = [
    ('ae','AE'),
    ('ats','ATS'),
    ('tam','TAM'),
    ('specialist','Specialist'),
    ('dir','Dir sales')
]

CATEGORY_CHOICES = [
    ('appsinfra','APPS & INFRA'),
    ('dataai','DATA & AI')
]

TECH_CHOICES = [
    ('aks','AKS'),
    ('bi', 'bBI'),
    ('bigdata','Big data (Databricks, HDI)'),
    ('devops','DevOps'),
    ('dwh','Data warehouse'),
    ('iot','IoT'),
    ('oss','Open Source'),
    ('sql','Migración SQL')
]

AREA_CHOICES = [
    ('rh', 'Recursos humanos'),
    ('ti', 'TI'),
    ('finanzas', 'Finanzas'),
    ('merca', 'Mercadotecnia'),
    ('seguridad', 'Seguridad')
]

class workRequest(models.Model):
    alias = models.CharField(max_length=50)
    creationDate = models.DateField(default=timezone.now)
    job_title = models.CharField(max_length=50,choices=JOB_TITLE_CHOICES,default="")
    engagement = models.CharField(max_length=10,default="")
    customer = models.CharField(max_length=50,default="")
    customer_area = models.CharField(max_length=50,choices=AREA_CHOICES,default="ti")
    request_title = models.CharField(max_length=100,default="")
    request_desc = models.CharField(max_length=200,default="")
    request_category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,default="")
    request_tech=models.CharField(max_length=50,choices=TECH_CHOICES,default="")
    request_date = models.DateField(default=timezone.now)
    
