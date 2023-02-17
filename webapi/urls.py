
from django.urls import path, include
from .views import (
    CountryApiView,
    RegionApiView
)

urlpatterns = [
    path('countries/', CountryApiView.as_view()),
    path('regions/', RegionApiView.as_view())
]