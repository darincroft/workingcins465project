from django.conf.urls import url
from django.contrib import admin
from . import views
 
app_name ='prj'
 
urlpatterns = [
"""
    url(r'^$', views.IndexView, name = 'index'),
    url(r'^prj/create_group/', views.CreateGroupView, name = 'create_group'),
    url(r'^prj/your_groups/', views.YourGroupsView, name = 'your_groups'),
    url(r'^prj/chat/', views.chat_view.as_view(), name = 'chat'),
"""
]

