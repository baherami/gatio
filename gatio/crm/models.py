from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    ssn = models.CharField(max_length=32)
    company_name = models.CharField(max_length=32)
    company_id = models.CharField(max_length=32)
    address = models.CharField(max_length=32)


class Seller(BaseUser):
    pass


class ScreenOwner(BaseUser):
    rate = models.IntegerField()
    credit = models.IntegerField()


class Advertiser(BaseUser):
    rate = models.IntegerField()
    credit = models.IntegerField()


class Contract(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

class Match(models.Model):
    screen_owner = models.ForeignKey(ScreenOwner, on_delete=models.CASCADE)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    frequency = models.IntegerField()
    price = models.IntegerField()

class Advertisement(models.Model):
    code = models.CharField(max_length=32)
    media_url = models.URLField()
    length = models.DurationField()
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)


class ScreenSpecifications(models.Model):
    code = models.CharField(max_length=30)
    size = models.IntegerField()


class Screen(models.Model):
    specification = models.ForeignKey(ScreenSpecifications, on_delete=models.CASCADE)
    screenowner = models.ForeignKey(ScreenOwner, on_delete=models.CASCADE)

