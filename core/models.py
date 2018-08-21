from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

LANGUAGE_CHOICES = settings.PROVIDER_LANGUAGES
CURRENCY_CHOICES = settings.PROVIDER_CURRENCIES


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='provider')
    name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='service_areas')
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    polygon = models.PolygonField()
