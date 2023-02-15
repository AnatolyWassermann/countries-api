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








# def country_generator(count):
#     country_list = []
#     random.shuffle(data)
#     for i in range(count):

#         country_name = data[i]['name'].get('common')
#         country_list.append(country_name)
#         country_capital = "".join(data[i]['capital'])
#         country_list.append(country_capital)
#         country_region = data[i]['region']
#         country_list.append(country_region)
#         country_area = data[i]['area']
#         country_list.append(country_area)
#         country_code = data[i]['cca2']
#         country_list.append(country_code)

#     print(country_list)
#     print(type(country_list))
#     print(len(country_list))
    

# country_generator(5)
# print(country_capital)
# print(country_region)
# print(country_area)
# print(country_name)

file.close()