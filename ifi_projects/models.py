from django.db import models

class Region(models.Model):

    name = models.CharField(max_length=200)

class Country(models.Model):

    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

class Project(models.Model):

    bank = models.CharField(max_length=200)
    project_number = models.CharField(max_length=200, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    local_cost = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=200, blank=True)
    usd_cost = models.IntegerField(blank=True, null=True)
    approval_date = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name + ' ' + self.bank