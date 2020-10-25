from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class ScreenOwner(Customer):
    pass


class Advertiser(Customer):
    pass


class Contract(models.Model):
    pass

class Match(models.Model):
    pass
    
class Screen(models.Model):
    code = models.CharField(max_length=30)


class Advertisement(models.Model):
    pass


class seller(models.Model):
    pass

