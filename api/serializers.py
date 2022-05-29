from rest_framework import serializers
from accountapp.models import Facebook, Page, Post, Group


class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facebook
        fields = ('__all__')


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
