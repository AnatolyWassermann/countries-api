
from django.urls import path, include
from .views import (
    CountryApiView,
    RegionApiView,
    CountryDetailApiView
)

urlpatterns = [
    path('countries/', CountryApiView.as_view()),
    path('regions/', RegionApiView.as_view()),
    path('countries/<int:country_id>/', CountryDetailApiView.as_view())
]