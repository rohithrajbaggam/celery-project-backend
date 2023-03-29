from django.db import models

# Create your models here.
class UserDataModel(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    countrycode = models.CharField(max_length=100)
    country = models.CharField(max_length=1000)
    bio = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    

    

