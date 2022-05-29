from django.db.models import fields
from accountapp.models import Facebook, Group, Page, Post, City, Country, station_list
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]


class FacebookForm(ModelForm):
    class Meta:
        model = Facebook
        exclude = ['id', 'fb_id']


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ("__all__")


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ['id', 'fb_id']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ("__all__")


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ("__all__")


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ("__all__")


class StationForm(ModelForm):
    class Meta:
        model = station_list
        fields = ("__all__")
