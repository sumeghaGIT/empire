# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from masters import views

urlpatterns = [
    url(r'^masters/locations/$', views.Locations.as_view(), name='locations'),
    # url(r'^masters/locations/delete/(?P<pk>[0-9]+)/$', views.RequestDeleteView.as_view(), name='delete_locations'),
    url(r'^masters/locations/delete/$', views.DeleteLocations.as_view(), name='delete_locations'),
    url(r'^masters/categories/$', views.CategoriesLists.as_view(), name='categories'),
    url(r'^masters/services/$', views.ServicesLists.as_view(), name='services'),
    url(r'^masters/services/add/$', views.CreateServices.as_view(), name='create_services'),
    url(r'^masters/services/edit/(?P<pk>[0-9]+)/$', views.UpdateServices.as_view(), name='update_services'),
    url(r'^createuser/$', views.CreateUser.as_view(), name="createuser"),
    url(r'^manageuser/$', views.ManageUser.as_view(), name="manageuser"),
    url(r'^masters/tasks/$', views.TaskStatus.as_view(), name='task_status'),
    url(r'^masters/inquiry/$', views.InquiryStatus.as_view(), name='inquiry_status'),
    url(r'^masters/inquiry/sources/$', views.InquirySources.as_view(), name='inquiry_sources'),
    url(r'^masters/departments/$', views.Departments.as_view(), name='departments'),
    url(r'^createticket/$', views.ticketView.as_view(), name="create_ticket"),
]
