
from django.urls import path, include
from .views import (
    CountryApiView,
)

urlpatterns = [
    path('api/', CountryApiView.as_view())
]