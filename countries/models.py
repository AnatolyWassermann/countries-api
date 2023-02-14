from django.db import models

class Capital(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
  

class Country(models.Model):
    name = models.CharField(max_length=30)
    capital = models.ForeignKey(Capital, on_delete= models.CASCADE)
    area = models.IntegerField()
    region = models.ForeignKey(Region, on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name






