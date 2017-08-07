# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    create_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField

    class Meta:
        db_table = "ebc_location"


class Categories(models.Model):
    category_name = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_categories"


class Services(models.Model):
    category = models.ManyToManyField(Categories)
    service_name = models.CharField(max_length=200, null=True)
    response_time = models.PositiveIntegerField()
    threshold_time = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_services"


class TaskStatus(models.Model):
    status = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_task_status"


class Notifications(models.Model):
    notification = models.CharField(max_length=200, null=True)
    imagePath = models.URLField(max_length=500, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_notifications"


class NotificationReadLog(models.Model):
    notification = models.OneToOneField(Notifications, on_delete=models.CASCADE)
    user_id = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_notification_read_log"


class InquiryStatus(models.Model):
    status = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_inquiry_status"


class InquirySources(models.Model):
    sources = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_inquiry_services"


class EmployeeStatus(models.Model):
    status = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_employee_status"


class EmployeeType(models.Model):
    employee_type = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_employee_table"


class Department(models.Model):
    department_name = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_department"


class InquiryActivity(models.Model):
    activity_name = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_inquiry_activity"
