from rest_framework import serializers

from .models import *


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionsContent
        fields = (
            "id",
            "name",
            "get_absolute_url_section",
            "content",
            "get_image",
            "get_thumbnail",
        )


class SectionsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = '__all__'
