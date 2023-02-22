
from django.urls import path
from .views import (
    CountryApiView,
    RegionApiView,
    CountryDetailApiView,
    RegionDetailApiView
)

urlpatterns = [
    path('countries/', CountryApiView.as_view()),
    path('regions/', RegionApiView.as_view()),
    path('countries/<int:pk>/', CountryDetailApiView.as_view()),
    path('regions/<int:pk>/', RegionDetailApiView.as_view())
]