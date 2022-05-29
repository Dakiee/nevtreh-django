from django.urls import path
from django.views.generic import TemplateView
from . import models

from . import views
from django.conf.urls import url
urlpatterns = [
    path('fb/', views.getFbApi, name='getFb'),
    path('list/', views.FBList.as_view(), name='list'),
    path('page/', views.PageList.as_view(), name='page'),
    path('post/', views.PostList.as_view(), name='post'),
    path('group/', views.GroupList.as_view(), name='group'),
    path('fourlist', views.showmultiplemodels)

]
