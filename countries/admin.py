from django.contrib import admin
from .models import Country, Region

class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'capital', 'region', 'area', 'code']

admin.site.register(Country, CountryAdmin)
admin.site.register(Region)
