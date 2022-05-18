from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class DataPoint(models.Model):
    user_UUID = models.CharField(max_length=36)
    user_code = models.CharField(max_length=8)
    app_version = models.CharField(max_length=300, blank=True, null=True)
    type = models.CharField(max_length=3, blank=True, null=True)
    encrypted_message = models.TextField(blank=True, null=True)
    encrypted_lon = models.TextField(blank=True)
    encrypted_lat = models.TextField(blank=True)
    encrypted_millisecondsSinceEpoch = models.TextField(blank=True, null=True)
    encrypted_speed = models.TextField(blank=True, null=True)
    encrypted_activity = models.TextField(blank=True, null=True)
    encrypted_altitude = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    encrypted_millisecondsSinceEpoch = models.PositiveBigIntegerField(blank=True, null=True)
    encrypted_speed = models.FloatField(blank=True, null=True)
    encrypted_activity = models.TextField(blank=True, null=True)
    encrypted_altitude = models.FloatField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'data point'
        verbose_name_plural = 'data points'

    def __unicode__(self):
        return str(self.id)


class AllowedIPs(models.Model):
    IP_address = models.GenericIPAddressField()
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'allowed IP address'
        verbose_name_plural = 'allowed IP addresses'