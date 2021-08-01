from django.db import models


# create a list you want to display on the header of the CRUD Table and then register them in admin.py and migrate them
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 70)
    email = models.CharField(max_length = 100)
    contact = models.CharField(max_length = 12)
