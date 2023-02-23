# Countries API

Countries API is my first API project. It contains all countries in the world and their respected regions with basic information.


## Description

I found a JSON file on Github containing information about all countries. Afterwards, I looped through this file and extracted the required information and added them to two different tables (countries, regions) in my PostgreSQL database. I converted the objects in this database into APIs using Django Rest Framework. The countries and regions pages, which are in the form of a list on the API, can be used with methods such as GET and POST. Also, when you go into their details, methods such as GET-POST-PUT and DELETE can also be used. For easy navigation, I have added HyperlinkedSerialization and Pagination. I used Token Authentication for Auth. Apart from actual API structure, I used python decouple to hide sensitive information and tested each new feature I added through POSTMAN.


## Installation
I added the required JSON file to the project.
 You can populate the tables in the database by running the command in dbobjects.py located in the project folder within the Django shell.