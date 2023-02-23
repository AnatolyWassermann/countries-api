
from django.urls import path
from .views import (
    CountryApiView,
    RegionApiView,
    CountryDetailApiView,
    RegionDetailApiView,
    CreateUserView,
    CustomAuthToken
)

urlpatterns = [
    path('countries/', CountryApiView.as_view()),
    path('regions/', RegionApiView.as_view()),
    path('countries/<int:pk>/', CountryDetailApiView.as_view()),
    path('regions/<int:pk>/', RegionDetailApiView.as_view()),
    path('createuser/', CreateUserView.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view())
]