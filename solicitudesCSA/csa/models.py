"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from dal import autocomplete

# Create your models here.

JOB_TITLE_CHOICES = [
    ('ae','AE'),
    ('ats','ATS'),
    ('tam','TAM'),
    ('specialist','Specialist'),
    ('dir','Dir sales')
]

AREA_CHOICES = [
    ('rh', 'Recursos humanos'),
    ('ti', 'TI'),
    ('finanzas', 'Finanzas'),
    ('merca', 'Mercadotecnia'),
    ('seguridad', 'Seguridad')
]

STATUS_CHOICES = [
    ('unknown', 'Unknown'),
    ('inprogress', 'In progress'),
    ('hold', 'On Hold'),
    ('finished', 'Finished'),
]

class AzureCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category name')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class AzureTechnology(models.Model):
    azureCategory = models.ForeignKey(AzureCategory,null=True, on_delete=models.CASCADE,default=0)
    name = models.CharField(max_length=100, verbose_name='Category name')

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class CSAuser(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name='Last name')
    alias = models.CharField(max_length=30, verbose_name='Alias')
    area = models.ForeignKey(AzureCategory,null=False, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.alias

class Customer(models.Model):
    tpid = models.IntegerField(verbose_name="TPID")
    name = models.CharField(max_length=50, verbose_name='Customer name')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class workRequest(models.Model):
    alias = models.CharField(max_length=50,verbose_name="Your alias")
    creationDate = models.DateField(default=timezone.now)
    job_title = models.CharField(max_length=50,choices=JOB_TITLE_CHOICES,default="")
    engagement = models.CharField(max_length=10,default="")
    customer = models.ForeignKey(Customer,null=True, on_delete=models.CASCADE)
    customer_area = models.CharField(max_length=50,choices=AREA_CHOICES,default="ti")
    request_title = models.CharField(max_length=100,default="")
    request_desc = models.CharField(max_length=200,default="")
    request_category = models.ForeignKey(AzureCategory,null=False, on_delete=models.CASCADE,default=1)
    request_tech=models.ForeignKey(AzureTechnology,null=True, on_delete=models.CASCADE,default=1)
    request_date = models.DateField(default=timezone.now,verbose_name="Expected Start Date")
    assigned_csa = models.ForeignKey(CSAuser,null=True, on_delete=models.CASCADE)
    request_status = models.CharField(max_length=50,choices=STATUS_CHOICES,default="unknown") 
    
    def __str__(self):
        return self.request_title

class workRequestUpdate(models.Model):
    modificationDate = models.DateField(default=timezone.now)
    workRequest = models.ForeignKey(workRequest,null=False, on_delete=models.CASCADE)
    csa = models.ForeignKey(CSAuser,null=True, on_delete=models.CASCADE)
    notification_status = models.IntegerField(verbose_name="notification_status",default=0) #0 not send 1 send
