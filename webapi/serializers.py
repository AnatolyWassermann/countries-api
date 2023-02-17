from rest_framework import serializers
from countries.models import Country, Region

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'capital', 'area', 'region', 'code', 'created', 'updated']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['name', 'area']

