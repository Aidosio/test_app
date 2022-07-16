from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class SectionsList(viewsets.ModelViewSet):
    queryset = SectionsContent.objects.all()
    serializer_class = SectionsSerializer


class SectionsNameList(viewsets.ModelViewSet):
    queryset = SectionsContent.objects.all()
    serializer_class = SectionsNameSerializer


class SectionsDetail(APIView):
    def get_object(self, section_slug, info_slug):
        try:
            return SectionsContent.objects.filter(pages__slug=section_slug).get(slug=info_slug)
        except SectionsContent.DoesNotExist:
            raise Http404

    def get(self, request, section_slug, info_slug, format=None):
        content = self.get_object(section_slug, info_slug)
        serializer_class = SectionsSerializer
        return Response(serializers.data)
