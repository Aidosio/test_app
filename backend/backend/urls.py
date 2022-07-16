from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from pages.views import *
from sections.views import *

pagesRoute = routers.SimpleRouter()
pagesRoute.register(r"pages", PagesList)

pagesNameRoute = routers.SimpleRouter()
pagesNameRoute.register(r"pagesname", PagesNameList)

sectionsRoute = routers.SimpleRouter()
sectionsRoute.register(r"sections", SectionsList)

sectionsNameRoute = routers.SimpleRouter()
sectionsNameRoute.register(r"sectionsname", SectionsNameList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include(pagesRoute.urls)),
    path('api/v1/', include(pagesNameRoute.urls)),
    path('api/v1/', include(sectionsRoute.urls)),
    path('api/v1/', include(sectionsNameRoute.urls)),
    path('api/v1/', include('pages.urls')),
    path('api/v1/', include('sections.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
