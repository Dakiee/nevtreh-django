import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class FacebookFilter(django_filters.FilterSet):
    class Meta:
        model = Facebook
        fields = '__all__'


class GroupFilter(django_filters.FilterSet):
    class Meta:
        model = Group
        fields = '__all__'


class PageFilter(django_filters.FilterSet):
    class Meta:
        model = Page
        fields = '__all__'


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['image']
