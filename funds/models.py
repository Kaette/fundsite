from django.db import models
from django.forms import ModelForm
# from fundsite.models import Fun

# Create your models here.

class Fund(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Investor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    creation_date = models.DateTimeField('date published')