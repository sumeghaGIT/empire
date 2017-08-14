# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from masters import views

urlpatterns = [
    url(r'^masters/locations/$', views.Locations.as_view(), name='locations'),
    # url(r'^masters/locations/delete/(?P<pk>[0-9]+)/$', views.RequestDeleteView.as_view(), name='delete_locations'),
    #url(r'^masters/locations/delete/$', views.DeleteLocations.as_view(), name='delete_locations'),
    url(r'^masters/categories/$', views.CategoriesLists.as_view(), name='categories'),
    #url(r'^masters/services/$', views.ServicesLists.as_view(), name='services'),
    url(r'^masters/services/$', views.CreateServices.as_view(), name='create_services'),
    url(r'^masters/services/edit/(?P<pk>[0-9]+)/$', views.UpdateServices.as_view(), name='update_services'),
    url(r'^masters/services/delete/(?P<pk>[0-9]+)/$', views.service_delete, name='delete_service'),
    url(r'^masters/location/edit/(?P<pk>[0-9]+)/$', views.UpdateLocations.as_view(), name='update_locations'),
    url(r'^masters/location/delete/(?P<pk>[0-9]+)/$', views.location_delete, name="delete_locations"),
    url(r'^masters/category/edit/(?P<pk>[0-9]+)/$', views.UpdateCategory.as_view(), name="update_category"),
    url(r'^masters/category/delete/(?P<pk>[0-9]+)/$', views.category_delete, name="delete_view"),
    url(r'^createuser/$', views.CreateUser.as_view(), name="createuser"),
    url(r'^manageuser/$', views.ManageUser.as_view(), name="manageuser"),
    url(r'^masters/tasks/$', views.TaskStatus.as_view(), name='task_status'),
    url(r'^masters/tasks/edit/(?P<pk>[0-9]+)/$', views.UpdateTaskStatus.as_view(), name='update_tasks'),
    url(r'^masters/tasks/delete/(?P<pk>[0-9]+)/$', views.task_status_delete, name="delete_tasks"),
    url(r'^masters/inquiry/$', views.InquiryStatus.as_view(), name='inquiry_status'),
    url(r'^masters/inquiry/edit/(?P<pk>[0-9]+)/$', views.UpdateInquiryStatus.as_view(), name='update_inquiry'),
    url(r'^masters/inquiry/delete/(?P<pk>[0-9]+)/$', views.inquiry_status_delete, name="delete_inquiry"),
    url(r'^masters/inquiry/sources/$', views.InquirySources.as_view(), name='inquiry_sources'),
    url(r'^masters/inquiry/sources/edit/(?P<pk>[0-9]+)/$', views.UpdateInquirySources.as_view(), name='update_inquiry_sources'),
    url(r'^masters/inquiry/sources/delete/(?P<pk>[0-9]+)/$', views.inquiry_sources_delete, name="delete_inquiry_sources"),
    url(r'^masters/departments/$', views.Departments.as_view(), name='departments'),
    url(r'^masters/department/edit/(?P<pk>[0-9]+)/$', views.UpdateDepartment.as_view(), name='update_department'),
    url(r'^masters/department/delete/(?P<pk>[0-9]+)/$', views.department_delete, name="delete_department"),
    url(r'^createticket/$', views.ticketView.as_view(), name="create_ticket"),
]
