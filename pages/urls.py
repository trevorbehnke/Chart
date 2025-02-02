# pages/urls.py
from django.urls import path

from .views import HomePageView, AboutPageView, ChartPageView


urlpatterns = [
    path('chart/', ChartPageView.as_view(), name='chart'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
