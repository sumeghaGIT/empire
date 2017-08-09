# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from reports import views

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	url(r'^$', views.indexView, name='index'),
]

# Create your tests here.
