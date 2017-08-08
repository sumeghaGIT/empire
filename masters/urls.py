# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from masters import views

urlpatterns = [
	url(r'^masters/$', views.Locations.as_view(), name='locations'),
	url(r'^masters/locations/create/$', views.CreateLocations.as_view(), name='create_locations'),
	# url(r'^masters/locations/create/$', views.create_location, name='create_locations'),
	# url(r'author/add/$', AuthorCreate.as_view(), name='author-add'),
]