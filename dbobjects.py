import json
from countries.models import Country, Region


file = open('countries.json')
data = json.load(file)



for i in range(len(data)):
    country_region = data[i]['region']
    country_name = data[i]['name'].get('common')
    country_capital = ", ".join(data[i]['capital'])
    country_area = data[i]['area']
    country_code = data[i]['cca2']
    Region.objects.get_or_create(name=country_region)
    country = Country.objects.create(name=country_name, 
                                     capital=country_capital, 
                                     area=country_area, 
                                     code=country_code, 
                                     region=Region.objects.get(name=country_region))
        

file.close()