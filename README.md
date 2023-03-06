# Countries API

Countries API is my first API project. It contains information of all countries in the world and their regions


## Description

I looped through a JSON file i found on Github and extracted the required information and added them to two different tables (countries, regions) in my PostgreSQL database. I converted the objects in this database into APIs using Django Rest Framework. The countries and regions pages, which are in the form of a list on the API, can be used with methods such as GET and POST. Also, when you go into their details, methods such as GET-POST-PUT and DELETE can also be used. For easy navigation, I have added HyperlinkedSerialization and Pagination. I used Token Authentication for Auth. Apart from actual API structure, I used python decouple to hide sensitive information and tested each new feature I added through POSTMAN.


## Installation
I added the required JSON file to the project.
 You can populate the tables in the database by running the command in dbobjects.py located in the project folder within the Django shell.
 ```python
''' -python manage.py shell- commands'''
import json
from countries.models import Country, Region


file = open('countries.json')
data = json.load(file)



for i in range(len(data)):
    country_region = data[i]['region']
    country_name = data[i]['name'].get('common')
    ''' added join method to separate if a country has more than 1 capital'''
    country_capital = ", ".join(data[i]['capital'])
    ''' if there is no capital '''
    if country_capital == "":
        country_capital = "None"
    country_area = data[i]['area']
    country_code = data[i]['cca2']
    ''' since region name field only allow unique names, i've used get_or_create method '''
    Region.objects.get_or_create(name=country_region)
    country = Country.objects.create(name=country_name, 
                                     capital=country_capital, 
                                     area=country_area, 
                                     code=country_code, 
                                     region=Region.objects.get(name=country_region))
        

file.close()
```
