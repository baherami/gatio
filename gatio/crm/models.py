from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=32)
    ssn = models.CharField(max_length=32)
    company_name = models.CharField(max_length=32)
    company_id = models.CharField(max_length=32)
    address = models.CharField(max_length=32)


class Contract(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()


class Match(models.Model):
    screen_owner = models.ForeignKey(Client, related_name="matchings_adds", on_delete=models.CASCADE)
    advertiser = models.ForeignKey(Client, related_name="matching_screens", on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    frequency = models.IntegerField()
    price = models.IntegerField()


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    user = instance.owner.id if instance.owner else "default_user"
    return 'user_{0}/{1}'.format(user, filename)


class MediaContent(models.Model):
    owner = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    code = models.CharField(max_length=32)
    media_file = models.FileField(upload_to=user_directory_path)
    media_length = models.DurationField()


class Advertisement(models.Model):
    media_content = models.ForeignKey(MediaContent, null=True, on_delete=models.CASCADE)
    advertiser = models.ForeignKey(Client, on_delete=models.CASCADE)


class ScreenSpecifications(models.Model):
    code = models.CharField(max_length=30)
    size = models.IntegerField()


class Screen(models.Model):
    specification = models.ForeignKey(ScreenSpecifications, on_delete=models.CASCADE)
    screen_owner = models.ForeignKey(Client,related_name="screens", default=None, on_delete=models.CASCADE)
    default_content = models.ForeignKey(MediaContent, null=True, on_delete=models.CASCADE)
    screen_client = models.OneToOneField(Client, related_name="machine", default=None, on_delete=models.CASCADE)
