from django.db import models
from django import forms

# Create your models here.
class NewsLetters(models.Model):
    """Newsletters model for maintening contact with users"""
    full_name = models.CharField(max_length=100, blank=True, null=True)
    fone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class VisiterData(models.Model):
    ip = models.GenericIPAddressField()
    city = models.CharField(max_length=100, blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    country_name = models.CharField(max_length=100, blank=True, null=True)
    dma_code = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    visits = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.ip 


class ContactMessage(models.Model):
    """ Message from a client """

    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    plan = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=10000)

    def __str__(self):
        return self.subject
