from rest_framework import serializers
from countries.models import Country, Region




class RegionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Region
        fields = ['id', 'name', 'area']
    
    
class ThousandSeparatorField(serializers.IntegerField):
    def to_representation(self, area):
        return f"{area:,}"
    


class CountrySerializer(serializers.ModelSerializer):
 
    region = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all())
    region_name = serializers.StringRelatedField(source='region', read_only=True)
    area = ThousandSeparatorField()
    class Meta:
        model = Country
        fields = ['id', 'name', 'capital', 'area', 'region', 'region_name', 'code', 'created', 'updated']

    



