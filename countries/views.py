from django.shortcuts import render
import json
import random
from .models import Country, Region

file = open('api_countries\countries.json')
data = json.load(file)

def country_generator(count):
    
    # country_list = []
    random.shuffle(data)
    for i in range(count):
        country_region = data[i]['region']
        Region.objects.create(name=country_region)
        country_name = data[i]['name'].get('common')
        Country.objects.create(name=country_name)
        country_capital = "".join(data[i]['capital'])
        Country.objects.create(capital=country_capital)
        country_area = data[i]['area']
        Country.objects.create(area=country_area)   
        country_code = data[i]['cca2']
        Country.objects.create(code=country_code)
        
   

country_generator(3)

# Create your views here.
file.close()