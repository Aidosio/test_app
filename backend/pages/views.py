from django.http import Http404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class PagesList(viewsets.ModelViewSet):
    queryset = PagesContent.objects.all()
    serializer_class = PagesSerializer


class PagesNameList(viewsets.ModelViewSet):
    queryset = Pages.objects.all()
    serializer_class = PagesNameSerializer


class PagesDetail(APIView):
    def get_object(self, pages_slug, content_slug):
        try:
            return PagesContent.objects.filter(pages__slug=pages_slug).get(slug=content_slug)
        except PagesContent.DoesNotExist:
            raise Http404

    def get(self, request, pages_slug, content_slug, format=None):
        content = self.get_object(pages_slug, content_slug)
        serializer_class = PagesSerializer
        return Response(serializers.data)