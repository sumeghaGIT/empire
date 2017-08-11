# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from masters import views
from django.contrib import admin
from .views import Notifications


admin.autodiscover()


urlpatterns = [
    url(r'^$', views.Notifications.as_view(), name='index'),

]
