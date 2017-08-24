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
    # business_hours = models.CharField(max_length=200, null=True)
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
    # taskstatus_from = models.CharField(max_length=4, null=True)
    # taskstatus_to = models.CharField(max_length=4, null=True)
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

class User(AbstractUser):
    department = models.PositiveIntegerField(max_length=4, blank=True, null=True)
    designation = models.PositiveIntegerField(max_length=4, blank=True, null=True)
    mobile = models.PositiveIntegerField(max_length=10, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ebc_user'
        ordering = ['-pk']

class TicketStatus(models.Model):
    status = models.CharField(max_length=60, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ebc_ticket_status'
        ordering = ['-pk']

class Ticket(models.Model):
    category =  models.ForeignKey(Categories, on_delete=models.CASCADE)
    service =  models.ForeignKey(Services, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)
    source = models.CharField(max_length=200, blank=True, null=True)
    status = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=200, blank=True, null=True)
    threshold_time = models.PositiveIntegerField(blank=True, null=True)
    # customer_type = models.CharField(max_length=200, blank=True, null=True)
    #  user = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)               # not in schema
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ebc_ticket'
        ordering = ['-pk']

class Customer(models.Model):
    first_name = models.CharField(unique=True, max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    # company_name = models.CharField(max_length=200, blank=True, null=True)
    # modile_number = models.CharField(max_length=200, blank=True, null=True)
    # office_phone = models.CharField(max_length=200, blank=True, null=True)
    # address1 = models.CharField(max_length=200, blank=True, null=True)
    # address2 = models.CharField(max_length=200, blank=True, null=True)
    # cityname = models.CharField(max_length=200, blank=True, null=True)
    # state_name = models.CharField(max_length=200, blank=True, null=True)
    # postalcode = models.CharField(max_length=200, blank=True, null=True)
    # country_name = models.CharField(max_length=200, blank=True, null=True)
    # website = models.CharField(max_length=200, blank=True, null=True)
    # vending_machine_no= models.CharField(max_length=200, blank=True, null=True)
    # telephone_extension = models.CharField(max_length=200, blank=True, null=True)
    # printer_name = models.CharField(max_length=200, blank=True, null=True)
    # account_manager = models.PositiveIntegerField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True) #not in schema
    password = models.CharField(max_length=200, blank=True, null=True) #not in schema
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ebc_customers'
        ordering = ['-pk']

class Dealsandoffers(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    approved_by = models.CharField(max_length=4, blank=True, null=True)
    remarks = models.CharField(max_length=2000, blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ebc_dealsandoffers'
        ordering = ['-pk']

class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_transaction = models.CharField(max_length=200, blank=True, null=True)
    payment_status = models.CharField(max_length=200, blank=True, null=True)
    transaction_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.PositiveIntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ebc_orders'
        ordering = ['-pk']

class OrderDetails(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)        #Product table is not in schema
    amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    other_charges = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ebc_orders_details'
        ordering = ['-pk']

class CustomerBilling(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    sale_amount =models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    discount_amount =models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    created_by = models.PositiveIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ebc_feedback'
        ordering = ['-pk']

# class Feedback(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
#     task_completedon_time = models.DateTimeField(blank=True, null=True)
#     staff_behaviour = models.CharField(max_length=200, blank=True, null=True)
#     service_rating = models.CharField(max_length=200, blank=True, null=True)
#     suggestions = models.CharField(max_length=500, blank=True, null=True)
#     created_by = models.PositiveIntegerField(blank=True, null=True)
#     create_date = models.DateTimeField(blank=True, null=True)
#     updated_by = models.PositiveIntegerField(blank=True, null=True)
#     update_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'ebc_feedback'
#         ordering = ['-pk']

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

class Inquiry(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    inquiry_details = models.CharField(max_length=200, null=True)
    source = models.ForeignKey(InquirySources, on_delete=models.CASCADE)
    status = models.ForeignKey(InquiryStatus, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=4, null=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    is_active = models.CharField(max_length=1, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.PositiveIntegerField()
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.PositiveIntegerField()

    class Meta:
        db_table = "ebc_inquiry"
        ordering = ['-pk']

    def __unicode__(self):
        return self.inquiry