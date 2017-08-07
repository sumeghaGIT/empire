# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.conf.urls import url
from reports import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]

# Create your tests here.
