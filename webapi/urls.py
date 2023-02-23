
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
    path('countries/<int:pk>/', CountryDetailApiView.as_view(), name='country_detail'),
    path('regions/<int:pk>/', RegionDetailApiView.as_view(), name='region_detail'),
    path('createuser/', CreateUserView.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view())
]