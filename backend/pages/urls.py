from django.urls import path, include

from pages import views

urlpatterns = [
    path('pages/<slug:pages_slug>/<slug:content_slug>/', views.PagesDetail.as_view())
]