from django.contrib import admin
from .models import Country, Region

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'capital', 'region', 'area_km2', 'code']
    ''' search function in admin page doesn't work with foreign keys so added __ to foreign key to work properly '''
    search_fields = ['name', 'capital', 'region__name', 'code']
    

admin.site.register(Country, CountryAdmin)
admin.site.register(Region)
