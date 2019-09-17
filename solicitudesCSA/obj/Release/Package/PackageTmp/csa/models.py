"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

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

class CSAuser(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    alias = models.CharField(max_length=30, verbose_name='Alias')

    def __str__(self):
        return self.alias

class workRequest(models.Model):
    alias = models.CharField(max_length=50,verbose_name="Your alias")
    creationDate = models.DateField(default=timezone.now)
    job_title = models.CharField(max_length=50,choices=JOB_TITLE_CHOICES,default="")
    engagement = models.CharField(max_length=10,default="")
    customer = models.CharField(max_length=50,default="")
    customer_area = models.CharField(max_length=50,choices=AREA_CHOICES,default="ti")
    request_title = models.CharField(max_length=100,default="")
    request_desc = models.CharField(max_length=200,default="")
    request_category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,default="")
    request_tech=models.CharField(max_length=50,choices=TECH_CHOICES,default="")
    request_date = models.DateField(default=timezone.now,verbose_name="Expected Start Date")
    assigned_csa = models.ForeignKey(CSAuser,null=True, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.request_title

