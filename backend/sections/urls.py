from django.urls import path, include

from sections import views

urlpatterns = [
    path('pages/<slug:section_slug>/<slug:info_slug>/', views.SectionsDetail.as_view())
]