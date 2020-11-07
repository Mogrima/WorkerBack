import datetime

from django.db import models
from django.utils import timezone

class Workers(models.Model):
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=100)
    position_name = models.CharField(max_length=100)
    hire_date = models.DateField('date hire_date', auto_now=False)
    fire_date = models.DateField('date fire_date', auto_now=False, null=True)
    salary = models.IntegerField()
    fraction = models.IntegerField()
    base = models.IntegerField()
    advance = models.IntegerField()
    by_hours = models.BooleanField()
    def __str__(self):
        return self.name
