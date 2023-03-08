# Countries API

Countries API is my first API project. It contains information of all countries in the world and their regions


## Description

I have extracted required information from a JSON file using a loop, which I found on Github, and added them to two separate tables, namely "countries" and "regions," in my PostgreSQL database. Next, I used Django Rest Framework to convert the objects in the database into APIs. The API for countries and regions pages is displayed in the form of a list, and they can be accessed using methods like GET and POST. When accessing the details, methods such as GET, POST, PUT, and DELETE can be utilized. To aid in ease of navigation, I implemented HyperlinkedSerialization and Pagination. Additionally, Token Authentication has been used for Auth. In order to protect sensitive information, I utilized python decouple, and all new features that were added have been tested thoroughly via POSTMAN.


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
