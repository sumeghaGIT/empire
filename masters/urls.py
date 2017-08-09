# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from masters import views

urlpatterns = [
    url(r'^masters/locations/$', views.Locations.as_view(), name='locations'),
    url(r'^masters/categories/$', views.CategoriesLists.as_view(), name='categories'),
    url(r'^masters/services/$', views.ServicesLists.as_view(), name='services'),
    url(r'^masters/services/add/$', views.CreateServices.as_view(), name='create_services'),
    url(r'^createuser/$', views.CreateUser.as_view(), name="createuser"),
    url(r'^manageuser/$', views.ManageUser.as_view(), name="manageuser"),
]
