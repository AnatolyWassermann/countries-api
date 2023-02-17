from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from countries.models import Region, Country
from .serializers import RegionSerializer, CountrySerializer

class CountryApiView(APIView):
    def get(self, request, *args, **kwargs):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):

        data = {
            'name': request.data.get('name'),
            'capital': request.data.get('capital'),
            'region': request.data.get('region'),
            'code': request.data.get('code'),
            'area': request.data.get('area')
        }

        serializer = CountrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
