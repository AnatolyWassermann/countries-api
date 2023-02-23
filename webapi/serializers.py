from rest_framework import serializers
from countries.models import Country, Region
from django.contrib.auth.models import User




class RegionSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "region_detail",
        lookup_field= "pk"
    )
    class Meta:
        model = Region
        fields = ['id', 'url', 'name', 'area']
    
    
class ThousandSeparatorField(serializers.IntegerField):
    def to_representation(self, area):
        return f"{area:,}"
    


class CountrySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = "country_detail",
        lookup_field = "pk"
    )
    region = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all())
    region_name = serializers.StringRelatedField(source='region', read_only=True)
    area = ThousandSeparatorField()
    class Meta:
        model = Country
        fields = ['id', 'url', 'name', 'capital', 'area', 'region', 'region_name', 'code', 'created', 'updated']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    



