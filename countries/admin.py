from django.contrib import admin
from .models import *

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capital', 'region', 'area')
    
admin.site.register(Capital)
admin.site.register(Country, CountryAdmin)
admin.site.register(Region)