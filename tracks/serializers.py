from rest_framework import serializers
from django.contrib.auth.models import User
from tracks.models import DataPoint


class DataPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataPoint
