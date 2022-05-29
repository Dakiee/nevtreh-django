from django.urls import path
from django.views.generic import TemplateView
from . import models

from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('fb/', views.FbCreate, name='facebook'),
    path('page/', views.PageCreate, name='page'),
    path('group/', views.GroupCreate, name='group'),
    path('post/', views.PostCreate, name='post'),
    path('fb_list/', views.Fb_list, name='fb_list'),
    path('post_list/', views.Post_list, name='post_list'),
    path('page_list/', views.Page_list, name='page_list'),
    path('group_list/', views.Group_list, name='group_list'),
    path('group/<int:pk>/edit/', views.editGroup, name="edit_group"),
    path('page/<int:pk>/edit/', views.editPage, name="edit_page"),
    path('post/<int:pk>/edit/', views.editPost, name="edit_post"),
    path('fb/<int:pk>/edit/', views.editFacebook, name="edit_fb"),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('bus', views.busmodels, name='bus'),
]
