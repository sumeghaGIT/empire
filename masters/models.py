# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class Location(models.Model):
    name = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=1, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField

    class Meta:
        db_table = "ebc_location"
        ordering = ['-pk']

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
        ordering = ['-pk']

    def __unicode__(self):
        return self.name


class Services(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    response_time = models.PositiveIntegerField(blank=True, null=True)
    threshold_time = models.PositiveIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    service_from = models.CharField(max_length=200, blank=True, null=True)
    service_to = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.CharField(max_length=1, default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_services"
        ordering = ['-pk']

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
        ordering = ['-pk']

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
        ordering = ['-pk']

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
        ordering = ['-pk']

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
        ordering = ['-pk']

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
        ordering = ['-pk']

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
        ordering = ['-pk']

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
        ordering = ['-pk']

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
        ordering = ['-pk']

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
        ordering = ['-pk']

    def __unicode__(self):
        return self.activity_name


class User(AbstractUser):
    user_type = models.CharField(max_length=2, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ebc_user'
        ordering = ['-pk']


class Ticket(models.Model):
    customer_type = models.CharField(max_length=200, blank=True, null=True)
    user = models.CharField(max_length=200, blank=True, null=True)
    ticket_type = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    service = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'ebc_ticket'
        ordering = ['-pk']


class Customer(models.Model):
    first_name = models.CharField(unique=True, max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ebc_customers'
        ordering = ['-pk']