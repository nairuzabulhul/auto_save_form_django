from __future__ import unicode_literals

from django.db import models

# Create your models here.
# from django.db import models
from jsonfield import JSONField

class Wizard(models.Model):
    data = JSONField()

# class Wizard(models.Model):
    
#     first_name = models.CharField(max_length=300)
#     last_name = models.CharField(max_length=300)
#     company_name = models.CharField(max_length=300)