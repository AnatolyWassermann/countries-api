from rest_framework import serializers
from countries.models import Country, Region




class RegionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Region
        fields = ['id', 'name', 'area']
    
    
class ThousandSeparatorField(serializers.IntegerField):
    def to_representation(self, area):
        return f"{area:,}"
    
# class RegionForeignKeyName(serializers.ReadOnlyField):
#     def to_representation(self, value):
#         region = Region.objects.all(id=value)
#         return region.name

class CountrySerializer(serializers.ModelSerializer):
    # ''' foreign key's name attribute will be shown rather than its ID '''
    # region = serializers.CharField(source='region.name', read_only=True)
    # region = RegionForeignKeyName(queryset=Region.objects.all())
    # region = RegionSerializer()
    
    area = ThousandSeparatorField()
    class Meta:
        model = Country
        fields = ['id', 'name', 'capital', 'area', 'region', 'code', 'created', 'updated']

    



