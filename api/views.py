from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from accountapp.models import Facebook, Page, Post, Group, station_list
from .serializers import FacebookSerializer, PageSerializer, PostSerializer, GroupSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from api import serializers
from rest_framework.response import Response


def getFbApi(request):
    if request.method in 'POST':
        print("create")
    elif request.method in 'DELETE':
        print("delete")
    elif request.method in 'PUT':
        print("uptade")
    elif request.method in 'GET':
        fb_list = Facebook.objects.all()
        serializer = FacebookSerializer(fb_list, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)


class PostList(generics.ListCreateAPIView):

    serializer_class = PostSerializer

    def get_queryset(request):
        queryset = Post.objects.all()
        # if get.para.page:
        return queryset


class GroupList(generics.ListCreateAPIView):

    serializer_class = GroupSerializer

    def get_queryset(request):
        queryset = Group.objects.all()
        # if get.para.page:
        return queryset


class FBList(generics.ListCreateAPIView):

    serializer_class = FacebookSerializer

    def get_queryset(request):
        queryset = Facebook.objects.all()
        # if get.para.page:
        return queryset


class PageList(generics.UpdateAPIView):

    serializer_class = PageSerializer

    def get_queryset(request):
        queryset = Page.objects.all()
        # if get.para.page:
        return queryset


@api_view(['GET'])
def showmultiplemodels(request):
    fbobj = Facebook.objects.all()
    pageobj = Page.objects.all()
    postobj = Post.objects.all()
    groupobj = Group.objects.all()
    FacebookSerializerobj = FacebookSerializer(fbobj, many=True)
    PageSerializerobj = PageSerializer(pageobj, many=True)
    PostSerializerobj = PostSerializer(postobj, many=True)
    GroupSerializerobj = GroupSerializer(groupobj, many=True)
    Resultmodel = FacebookSerializerobj.data+PageSerializerobj.data + \
        PostSerializerobj.data+GroupSerializerobj.data
    return Response(Resultmodel)
