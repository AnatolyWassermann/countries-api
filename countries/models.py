from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=30, unique=True, null=True)
    area = models.IntegerField(default=1)
    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    capital = models.CharField(max_length=30, unique=True, null=True)
    area = models.IntegerField(default=1)
    code = models.CharField(max_length=10, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name