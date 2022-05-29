from django.db import models
from django.forms import widgets


class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Facebook(models.Model):
    user_name = models.CharField(max_length=255, null=True, blank=True)
    fb_id = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    mobile = models.CharField(max_length=255)
    country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, blank=True, null=True)
    friends = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    link = models.URLField(max_length=200, null=True)

    def __str__(self):
        return str(self.user_name)


class Page(models.Model):
    owner = models.ForeignKey(
        Facebook, on_delete=models.CASCADE, null=True, blank=True)
    like = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    page_type = models.CharField(max_length=255)
    mobile = models.IntegerField(default=0)
    email = models.CharField(max_length=100)
    link = models.URLField(max_length=200, null=True)

    def __str__(self):
        return str(self.email)


class Group(models.Model):
    fb_id = models.CharField(max_length=255)
    admin = models.ForeignKey(
        Facebook, on_delete=models.CASCADE, null=True, blank=True)
    moderator = models.CharField(max_length=255)
    members = models.IntegerField(default=0)
    privacy = models.CharField(max_length=50)
    visible = models.CharField(max_length=50)
    group_type = models.CharField(max_length=50)
    rules = models.CharField(max_length=1000)
    link = models.URLField(max_length=200, null=True)

    def __str__(self):
        return str(self.moderator)


class Post(models.Model):
    owner = models.ForeignKey(Facebook, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    like = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    link = models.URLField(max_length=200, null=True)
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100, null=True)

    def __str__(self):
        return str(self.link)


class station_list(models.Model):
    station_name = models.CharField(max_length=255)
    station_id = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
    station_seq = models.IntegerField(default=0)
    exist_bus = models.CharField(max_length=10)
    latitude = models.IntegerField(default=0)


class bus_info(models.Model):
    bus_id = models.IntegerField()
