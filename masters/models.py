# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as BaseUser


class Location(models.Model):
    name = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField

    class Meta:
        db_table = "ebc_location"

    def __unicode__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_categories"

    def __unicode__(self):
        return self.name


class Services(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    response_time = models.PositiveIntegerField(blank=True, null=True)
    threshold_time = models.PositiveIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    service_from = models.TimeField(auto_now_add=True, blank=True)
    service_to = models.TimeField(auto_now_add=True, blank=True)
    is_active = models.CharField(max_length=1, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_services"

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return u'/masters/services/edit/%d' % self.id


class TaskStatus(models.Model):
    status = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_task_status"

    def __unicode__(self):
        return self.status


class Notifications(models.Model):
    notification = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    imagePath = models.URLField(max_length=500, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_notifications"

    def __unicode__(self):
        return self.notification


class NotificationReadLog(models.Model):
    notification = models.ForeignKey(Notifications, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    user_id = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_notification_read_log"

    def __unicode__(self):
        return self.notification


class InquiryStatus(models.Model):
    status = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_inquiry_status"

    def __unicode__(self):
        return self.status


class InquirySources(models.Model):
    sources = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_inquiry_services"

    def __unicode__(self):
        return self.sources


class EmployeeStatus(models.Model):
    status = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_employee_status"

    def __unicode__(self):
        return self.status


class EmployeeType(models.Model):
    employee_type = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_employee_table"

    def __unicode__(self):
        return self.employee_type


class Department(models.Model):
    name = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_department"

    def __unicode__(self):
        return self.name


class InquiryActivity(models.Model):
    activity_name = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_inquiry_activity"

    def __unicode__(self):
        return self.activity_name


class UserType(models.Model):
    user_type = models.CharField(unique=True, max_length=2, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.PositiveIntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField()
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebc_user_type'

    def __unicode__(self):
        return self.user_type


class User(BaseUser):
    # username = models.CharField(unique=True, max_length=64, blank=True, null=True)
    # is_active = models.CharField(max_length=1, blank=True, null=True)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ebc_user'
