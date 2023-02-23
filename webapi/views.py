
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from countries.models import Region, Country
from .serializers import RegionSerializer, CountrySerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CountryApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Country.objects.all()
    serializer_class = CountrySerializer



# class CountryApiView(APIView):
#     def get(self, request, *args, **kwargs):
#         countries = Country.objects.all()
#         serializer = CountrySerializer(countries, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):

#         data = {
#             'name': request.data.get('name'),
#             'capital': request.data.get('capital'),
#             'region': request.data.get('region'),
#             'code': request.data.get('code'),
#             'area': request.data.get('area')
#         }

#         serializer = CountrySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegionApiView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

# class RegionApiView(APIView):
#     def get(self, request, *args, **kwargs):
#         regions = Region.objects.all()
#         serializer = RegionSerializer(regions, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):

#         data = {
#             'name': request.data.get('name'),
#             'area': request.data.get('area')
#         }

#         serializer = RegionSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class CountryDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'pk'


    
    
    
    
    
# class CountryDetailApiView(APIView):
    
#     def get_object(self, country_id):
#         """get method"""
#         try:
#             return Country.objects.get(id=country_id)
#         except:
#             return None
        
#     def get(self, request, country_id, *args, **kwargs):
#         """retrieve"""

#         country_instance = self.get_object(country_id)
#         if not country_instance:
#             return Response(
#                 {"res": "Object with country id does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         serializer = CountrySerializer(country_instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, country_id, *args, **kwargs):
#         """ updates the item if exists"""
#         country_instance = self.get_object(country_id)
#         if not country_instance:
#             return Response(
#                 {"res": "Object with country id not exists"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {
#         'name': request.data.get('name'),
#         'capital': request.data.get('capital'),
#         'region': request.data.get('region'),
#         'code': request.data.get('code'),
#         'area': request.data.get('area')
#         }
#         serializer = CountrySerializer(instance = country_instance, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def delete(self, request, country_id, *args, **kwargs):
#         '''
#         Deletes the country item if exists
#         '''
#         country_instance = self.get_object(country_id)
#         if not country_instance:
#             return Response(
#                 {"res": "Object with country id does not exists"}, 
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         country_instance.delete()
#         return Response(
#             {"res": f"Object: {country_instance} deleted!"},
#             status=status.HTTP_200_OK
#         )

class RegionDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    lookup_field = 'pk'


class CreateUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'user_name': user.username,
            'email': user.email
        })
