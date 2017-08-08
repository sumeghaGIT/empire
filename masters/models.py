# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    create_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField

    class Meta:
        db_table = "ebc_location"


class Categories(models.Model):
    category_name = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_categories"


class Services(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=1, blank=True, null=True)
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
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_task_status"


class Notifications(models.Model):
    notification = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    imagePath = models.URLField(max_length=500, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_notifications"


class NotificationReadLog(models.Model):
    notification = models.ForeignKey(Notifications, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    user_id = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_notification_read_log"


class InquiryStatus(models.Model):
    status = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_inquiry_status"


class InquirySources(models.Model):
    sources = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_inquiry_services"


class EmployeeStatus(models.Model):
    status = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_employee_status"


class EmployeeType(models.Model):
    employee_type = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_employee_table"


class Department(models.Model):
    department_name = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_department"


class InquiryActivity(models.Model):
    activity_name = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField()
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_inquiry_activity"


class UserType(models.Model):
    user_type = models.CharField(unique=True, max_length=2, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.PositiveIntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField()
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebc_user_type'

        def __str__(self):
            return self.name


class User(models.Model):
    username = models.CharField(unique=True, max_length=64, blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    user_type = models.ForeignKey(UserType, models.DO_NOTHING)
    created_by = models.PositiveIntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField()
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebc_user'