from django.urls import path
from apps.scraping.views.view import ScrapingView

urlpatterns = [
    path('', ScrapingView.as_view(), name='scrap'),
]
