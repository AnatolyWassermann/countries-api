from rest_framework import serializers
from countries.models import Country, Region
from django.utils.formats import number_format

class CountrySerializer(serializers.ModelSerializer):
    ''' foreign key's name attribute will be shown rather than its ID '''
    region = serializers.CharField(source='region.name')
    area = serializers.SerializerMethodField('area_localizer')
    class Meta:
        model = Country
        fields = ['id', 'name', 'capital', 'area', 'region', 'code', 'created', 'updated']

    def area_localizer(self, obj):
        return f"{obj.area:,}"

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'area']

