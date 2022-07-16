from rest_framework import serializers

from .models import *


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagesContent
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "content",
            "get_image",
            "get_thumbnail",
        )


class PagesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = '__all__'
