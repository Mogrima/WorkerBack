from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone

# type Workers {
#   name: String!,
#   companyName: String!,
#   positionName: String!,
#   hireDate: Date!,
#   fireDate: Date,
#   salary: Int!,
#   fraction: Int!,
#   base: Int!,
#   advance: Int!,
#   by_hours: Boolean!
# }

# type Query {  
#   actor(id: ID!): Actor
#   actors: [Actor]
# }

# input WorkersInput {
#     id: ID
#     name: String!
# }

# type  WorkersPayload {  
#   ok: Boolean
#   work: Workers
# }


class Workers(models.Model):
    name = models.CharField(max_length=200)
    companyName = models.CharField(max_length=100)
    position_name = models.CharField(max_length=100)
    hire_date = models.DateField('date hire_date', auto_now=False)
    fire_date = models.DateField(
        'date fire_date', auto_now=False, null=True, blank=True)
    salary = models.IntegerField()
    fraction = models.IntegerField()
    base = models.IntegerField()
    advance = models.IntegerField()
    by_hours = models.BooleanField()

    def __str__(self):
        return self.name
