# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from django.views import View
from django.dispatch import receiver
from django.db.models.signals import post_save
from channels import Group
from masters import models
from django.contrib.auth import get_user_model

User = get_user_model()

from masters.forms import *
from masters.models import Categories, Services, Dealsandoffers, Customer

class Locations(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = LocationsForm
    initial = {'location_name': ''}
    template_name = 'locations/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        locations = models.Location.objects.all()
        return render(request, self.template_name, {'locations':locations,'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            time_now = datetime.datetime.utcnow()
            location = models.Location.objects.create(
                    name=form.cleaned_data['location_name'],
                    is_active= form.cleaned_data['status'],
                    created_by=request.user.id,
                    updated_date=time_now
            )
            return HttpResponseRedirect('/masters/locations/')
        locations = models.Location.objects.all()
        return render(request, self.template_name, {'form': form, 'locations':locations})


class UpdateLocations(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = LocationsForm
    initial = {'location_name': ''}
    template_name = 'locations/edit.html'

    def get(self, request, *args, **kwargs):
        data = {}
        if 'pk' in kwargs and kwargs['pk'] is not None:
            location = models.Location.objects.get(id=kwargs['pk'])
            data = {'location_name': location.name,
                    'is_active': location.is_active,
                    'created_date': location.created_date,
                    'updated_by': location.updated_by,
                    }
        form = LocationsForm(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if 'pk' in kwargs and kwargs['pk'] is not None:
                location = models.Location.objects.get(id=kwargs['pk'])
                location.name = form.cleaned_data['location_name']
                location.is_active = form.cleaned_data['status']
                location.updated_by = request.user.id
                location.save()
            return HttpResponseRedirect('/masters/locations/')
        return render(request, self.template_name, {'form': form})


def location_delete(request, pk):

    try:
        location = models.Location.objects.filter(id=pk)
    except:
        location = None
    if location is not None:
        location.delete()
        return HttpResponse("success")
        # return HttpResponseRedirect('/masters/locations/')


class CategoriesLists(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = CategoriesForm
    initial = {'category_name': ''}
    template_name = 'categories/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        categories = models.Categories.objects.all()
        return render(request, self.template_name, {'categories':categories, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            location = models.Categories.objects.create(
                    name=form.cleaned_data['category_name'],
                    created_by=request.user.id,
                    updated_by=request.user.id,
                    is_active= form.cleaned_data['status']
            )
            return HttpResponseRedirect('/masters/categories/')
        categories = models.Categories.objects.all()
        return render(request, self.template_name, {'categories':categories, 'form': form})


class UpdateCategory(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = CategoriesForm
    initial = {'category_name': ''}
    template_name = 'categories/edit.html'

    def get(self, request, *args, **kwargs):
        data = {}
        if 'pk' in kwargs and kwargs['pk'] is not None:
            category = models.Categories.objects.get(id=kwargs['pk'])
            data = {'category_name': category.name,
                    'is_active': category.is_active,
                    'created_date': category.created_date,
                    'updated_by': category.updated_by,
                    }
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if 'pk' in kwargs and kwargs['pk'] is not None:
                category = models.Categories.objects.get(id=kwargs['pk'])
                category.name = form.cleaned_data['category_name']
                category.is_active = form.cleaned_data['status']
                category.updated_by = request.user.id
                category.save()
            return HttpResponseRedirect('/masters/categories/')
        return render(request, self.template_name, {'form': form})


def category_delete(request, pk):

    try:
        category = models.Categories.objects.filter(id=pk)
    except:
        category = None
    if category is not None:
        category.delete()
        return HttpResponse("success")
        # return HttpResponseRedirect('/masters/categories/')


class CreateServices(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = ServicesForm
    initial = {'service_name': ''}
    template_name = 'services/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        services = models.Services.objects.all()
        return render(request, self.template_name, {'services': services, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        print form
        if form.is_valid():
            services = models.Services.objects.create(
                    name=form.cleaned_data['service_name'],
                    category_id=int(form.cleaned_data['category_name'].id),
                    response_time=form.cleaned_data['response_time'],
                    threshold_time=form.cleaned_data['threshold_time'],
                    price=form.cleaned_data['price'],
                    service_from=form.cleaned_data['service_from'],
                    service_to=form.cleaned_data['service_to'],
                    is_active=form.cleaned_data['status'],
                    created_by=request.user.id,
                    updated_by=request.user.id,
            )
            return HttpResponseRedirect('/masters/services/')
        services = models.Services.objects.all()
        return render(request, self.template_name, {'services': services, 'form': form})


class UpdateServices(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = ServicesForm
    initial = {'service_name': ''}
    template_name = 'services/edit.html'

    def get(self, request, *args, **kwargs):
        data = {}
        if 'pk' in kwargs and kwargs['pk'] is not None:
            services = models.Services.objects.get(id=kwargs['pk'])
            data = {'service_name': services.name,
                    'response_time': services.response_time,
                    'threshold_time': services.threshold_time,
                    'category_name': services.category_id,
                    'price': services.price,
                    'service_from': services.service_from,
                    'service_to': services.service_to,
                    'is_active': services.is_active,
                    }
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if 'pk' in kwargs and kwargs['pk'] is not None:
                services = models.Services.objects.get(id=kwargs['pk'])
                services.name = form.cleaned_data['service_name']
                services.category_id=form.cleaned_data['category_name']
                services.response_time=form.cleaned_data['response_time']
                services.threshold_time=form.cleaned_data['threshold_time']
                services.price=form.cleaned_data['price']
                services.service_from=form.cleaned_data['service_from']
                services.service_to=form.cleaned_data['service_to']
                services.is_active=form.cleaned_data['status']
                services.updated_by=request.user.id
                services.save()
            return HttpResponseRedirect('/masters/services/')
        return render(request, self.template_name, {'form': form})


def service_delete(request, pk):

    try:
        service = models.Services.objects.filter(id=pk)
    except:
        service = None
    if service is not None:
        service.delete()
        return HttpResponse("success")
        # return HttpResponseRedirect('/masters/services/')


class ServicesByCategory(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):
        category_id = kwargs['id']
        services = models.Services.objects.filter(category_id = category_id, is_active = 1)
        result_list = list(services.values('id', 'name'))
        return HttpResponse(json.dumps(result_list) , content_type="application/json")
        

class TaskStatus(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = TaskStatusForm
    initial = {'tasks': ''}
    template_name = 'status/tasks_status.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        tasks = models.TaskStatus.objects.all()
        return render(request, self.template_name, {'results':tasks,'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            location = models.TaskStatus.objects.create(
                    status=form.cleaned_data['name'],
                    created_by=request.user.id,
                    updated_by=request.user.id,
                    is_active= form.cleaned_data['status'],
            )
            return HttpResponseRedirect('/masters/tasks/')
        tasks = models.TaskStatus.objects.all()
        return render(request, self.template_name, {'results':tasks,'form':form})


class UpdateTaskStatus(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = TaskStatusForm
    initial = {'name': ''}
    template_name = 'status/edit_task_status.html'

    def get(self, request, *args, **kwargs):
        data = {}
        if 'pk' in kwargs and kwargs['pk'] is not None:
            task_status = models.TaskStatus.objects.get(id=kwargs['pk'])
            data = {'name': task_status.status,
                    'is_active': task_status.is_active,
                    'created_date': task_status.created_date,
                    'updated_by': task_status.updated_by,
                    }
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if 'pk' in kwargs and kwargs['pk'] is not None:
                task_status = models.TaskStatus.objects.get(id=kwargs['pk'])
                task_status.status = form.cleaned_data['name']
                task_status.is_active = form.cleaned_data['status']
                task_status.updated_by = request.user.id
                task_status.save()
            return HttpResponseRedirect('/masters/tasks/')
        return render(request, self.template_name, {'form': form})


def task_status_delete(request, pk):

    try:
        task_status = models.TaskStatus.objects.filter(id=pk)
    except:
        task_status = None
    if task_status is not None:
        task_status.delete()
        return HttpResponse("success")
        # return HttpResponseRedirect('/masters/tasks/')


class InquiryStatus(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = TaskStatusForm
    initial = {'tasks': ''}
    template_name = 'status/inquiry_status.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        inquiries = models.InquiryStatus.objects.all()
        return render(request, self.template_name, {'results':inquiries,'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            location = models.InquiryStatus.objects.create(
                    status=form.cleaned_data['name'],
                    created_by=request.user.id,
                    updated_by=request.user.id,
                    is_active= form.cleaned_data['status'],
            )
            return HttpResponseRedirect('/masters/inquiry/')
        inquiries = models.InquiryStatus.objects.all()
        return render(request, self.template_name, {'results':inquiries,'form':form})


class UpdateInquiryStatus(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = TaskStatusForm
    initial = {'name': ''}
    template_name = 'status/edit_inquiry_status.html'

    def get(self, request, *args, **kwargs):
        data = {}
        if 'pk' in kwargs and kwargs['pk'] is not None:
            inquiry_status = models.InquiryStatus.objects.get(id=kwargs['pk'])
            data = {'name': inquiry_status.status,
                    'is_active': inquiry_status.is_active,
                    'created_date': inquiry_status.created_date,
                    'updated_by': inquiry_status.updated_by,
                    }
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if 'pk' in kwargs and kwargs['pk'] is not None:
                inquiry_status = models.InquiryStatus.objects.get(id=kwargs['pk'])
                inquiry_status.status = form.cleaned_data['name']
                inquiry_status.is_active = form.cleaned_data['status']
                inquiry_status.updated_by = request.user.id
                inquiry_status.save()
            return HttpResponseRedirect('/masters/inquiry/')
        return render(request, self.template_name, {'form': form})


def inquiry_status_delete(request, pk):

    try:
        task_status = models.InquiryStatus.objects.filter(id=pk)
    except:
        task_status = None
    if task_status is not None:
        task_status.delete()
        return HttpResponse("success")


class InquirySources(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = TaskStatusForm
    initial = {'tasks': ''}
    template_name = 'status/inquiry_sources.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        sources = models.InquirySources.objects.all()
        return render(request, self.template_name, {'results':sources,'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            location = models.InquirySources.objects.create(
                    sources=form.cleaned_data['name'],
                    created_by=request.user.id,
                    updated_by=request.user.id,
                    is_active= form.cleaned_data['status'],
            )
            return HttpResponseRedirect('/masters/inquiry/sources/')
        sources = models.InquirySources.objects.all()
        return render(request, self.template_name, {'results':sources,'form':form})


class UpdateInquirySources(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = TaskStatusForm
    initial = {'name': ''}
    template_name = 'status/edit_inquiry_sources.html'

    def get(self, request, *args, **kwargs):
        data = {}
        if 'pk' in kwargs and kwargs['pk'] is not None:
            inquiry_sources = models.InquirySources.objects.get(id=kwargs['pk'])
            data = {'name': inquiry_sources.sources,
                    'is_active': inquiry_sources.is_active,
                    'created_date': inquiry_sources.created_date,
                    'updated_by': inquiry_sources.updated_by,
                    }
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if 'pk' in kwargs and kwargs['pk'] is not None:
                inquiry_sources = models.InquirySources.objects.get(id=kwargs['pk'])
                inquiry_sources.sources = form.cleaned_data['name']
                inquiry_sources.is_active = form.cleaned_data['status']
                inquiry_sources.updated_by = request.user.id
                inquiry_sources.save()
            return HttpResponseRedirect('/masters/inquiry/sources/')
        return render(request, self.template_name, {'form': form})


def inquiry_sources_delete(request, pk):

    try:
        inquiry_sources = models.InquirySources.objects.filter(id=pk)
    except:
        inquiry_sources = None
    if inquiry_sources is not None:
        inquiry_sources.delete()
        return HttpResponse("success")
        # return HttpResponseRedirect('/masters/inquiry/sources/')


class Departments(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = TaskStatusForm
    initial = {'tasks': ''}
    template_name = 'status/departments.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        department = models.Department.objects.all()
        return render(request, self.template_name, {'results':department,'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            location = models.Department.objects.create(
                    name=form.cleaned_data['name'],
                    created_by=request.user.id,
                    updated_by=request.user.id,
                    is_active= form.cleaned_data['status'],
            )
            return HttpResponseRedirect('/masters/departments/')
        department = models.Department.objects.all()
        return render(request, self.template_name, {'results':department,'form':form})


class UpdateDepartment(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = TaskStatusForm
    initial = {'name': ''}
    template_name = 'status/edit_department.html'

    def get(self, request, *args, **kwargs):
        data = {}
        if 'pk' in kwargs and kwargs['pk'] is not None:
            department = models.Department.objects.get(id=kwargs['pk'])
            data = {'name': department.name,
                    'is_active': department.is_active,
                    'created_date': department.created_date,
                    'updated_by': department.updated_by,
                    }
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if 'pk' in kwargs and kwargs['pk'] is not None:
                department = models.Department.objects.get(id=kwargs['pk'])
                department.name = form.cleaned_data['name']
                department.is_active = form.cleaned_data['status']
                department.updated_by = request.user.id
                department.save()
            return HttpResponseRedirect('/masters/departments/')
        return render(request, self.template_name, {'form': form})


def department_delete(request, pk):

    try:
        department = models.Department.objects.filter(id=pk)
    except:
        department = None
    if department is not None:
        department.delete()
        return HttpResponse('success')


class UpdateUser(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = UpdateUserForm
    initial = {'username': ''}
    template_name = 'allauth/templates/account/edit_user.html'

    def get(self, request, *args, **kwargs):
        data = {}
        if 'pk' in kwargs and kwargs['pk'] is not None:
            user = User.objects.get(id=kwargs['pk'])
            data = {'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'is_active': user.is_active,
                    'created_by': request.user.id,
                    }
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if 'pk' in kwargs and kwargs['pk'] is not None:
                user = User.objects.get(id=kwargs['pk'])
                user.username = form.cleaned_data['username']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.is_active = form.cleaned_data['status']
                user.updated_by = request.user.id
                user.save()
            return HttpResponseRedirect('/manageuser')
        return render(request, self.template_name, {'form': form})


class CreateUser(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        return render(request, 'allauth/templates/account/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                is_active=True,
                user_type=form.cleaned_data['user_type'],
            )
            if user:
                user.set_password(form.cleaned_data['password1'])
                user.save()
            return HttpResponseRedirect('/manageuser')
        else:
            return render(request, 'allauth/templates/account/create.html', {'form': form})


class ManageUser(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        return render(request, 'allauth/templates/account/manageuser.html', {'users': user})


def user_delete(request, pk):

    try:
        user = User.objects.filter(id=pk)
    except:
        user = None
    if user is not None:
        user.delete()
        return HttpResponseRedirect('/manageuser')


class Customers(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = CustomerCreateForm
    initial = {'first_name': ''}
    template_name = 'customers/create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        customer = models.Customer.objects.all()
        return render(request, self.template_name, {'customers': customer, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            customer = models.Customer.objects.create(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password1'],
                    is_active='Y',
                    created_by=request.user.id,
                    updated_by=request.user.id
            )
            return HttpResponseRedirect('/masters/customers/')
        customer = models.Customer.objects.all()
        return render(request, self.template_name, {'form': form, 'customers': customer})


class UpdateCustomers(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = UpdateCreateForm
    initial = {'first_name': ''}
    template_name = 'customers/edit.html'

    def get(self, request, *args, **kwargs):
        data = {}
        if 'pk' in kwargs and kwargs['pk'] is not None:
            customer = models.Customer.objects.get(id=kwargs['pk'])
            data = {'first_name': customer.first_name,
                    'last_name': customer.last_name,
                    'created_date': customer.create_date,
                    'updated_by': customer.updated_by,
                    }
        form = UpdateCreateForm(initial=data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if 'pk' in kwargs and kwargs['pk'] is not None:
                customer = models.Customer.objects.get(id=kwargs['pk'])
                customer.first_name = form.cleaned_data['first_name']
                customer.last_name = form.cleaned_data['last_name']
                customer.is_active = form.cleaned_data['status']
                customer.updated_by = request.user.id
                customer.save()
            return HttpResponseRedirect('/masters/customers/')
        return render(request, self.template_name, {'form': form})


def customer_delete(request, pk):

    try:
        customer = models.Customer.objects.filter(id=pk)
    except:
        customer = None
    if customer is not None:
        customer.delete()
        return HttpResponse("success")


class CreateTickets(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = CreateTicketForm
    initial = {'service_name': ''}
    template_name = 'notifications/create_ticket.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        ticket = models.Ticket.objects.all()
        user = User.objects.all()
        category = Categories.objects.all()
        service = Services.objects.all()
        return render(request, self.template_name, {'form': form, 'user': user, 'category':category, 'service':service})

    def post(self, request, *args, **kwargs):
        form = CreateTicketForm(request.POST)

        ticket = models.Ticket.objects.create(ticket_type=request.POST.get('ticket_type'),
                                              category=request.POST.get('category_name'),
                                              service=request.POST.get('service_name'),
                                              comment=request.POST.get('comment'),
                                              is_active='Y')
        post_save.connect(ticket_created, sender=models.Ticket)
        notification_count = models.Ticket.objects.filter(is_active='Y').count()
        return JsonResponse({'notification_count': notification_count})


@receiver(post_save, sender=models.Notifications)
def ticket_created(sender, instance, **kwargs):
    notification_count = models.Ticket.objects.filter(is_active='Y').count()
    if kwargs.get('created', False):
        Group("notification").send({
            "text": json.dumps({
                "count": notification_count,
                "content": instance.comment
            })
        })



class AllCategories(LoginRequiredMixin, View):
    """ List all the categories """

    def get(self, request, *args, **kwargs):
        return JsonResponse(list(Categories.objects.values()), safe=False )

class ActiveCategory(LoginRequiredMixin, View):
    """ List all the active categories """

    def get(self, request, *args, **kwargs):
        category = Categories.objects.filter(is_active=1).values()
        return JsonResponse(list(category), safe=False )
        # # category = list(category.values('id', 'name'))
        # return HttpResponse(json.dumps(category), content_type="application/json")

class GetCategory(LoginRequiredMixin, View):
    """ Get the category by id """

    def get(self, request, *args, **kwargs):
        category_id = kwargs['id']
        data = list(Categories.objects.filter(id=category_id, is_active=1).values())
        return JsonResponse(data, safe=False)

class AllServices(LoginRequiredMixin, View):
    """ List all the Services """

    def get(self, request, *args, **kwargs):
        return JsonResponse(list(Services.objects.values()), safe=False )

class ActiveServices(LoginRequiredMixin, View):
    """ List all the active Services """

    def get(self, request, *args, **kwargs):
        service_value = Services.objects.filter(is_active=1).values()
        return JsonResponse(list(service_value), safe=False )

class GetService(LoginRequiredMixin, View):
    """ Get the Services by id """

    def get(self, request, *args, **kwargs):
        service_id = kwargs['id']
        service_value = list(Services.objects.filter(id=service_id, is_active=1).values())
        return JsonResponse(service_value, safe=False)

class CategoryServicesDetails(LoginRequiredMixin, View):
    """ Get list of services by category id """

    def get(self, request, *args, **kwargs):
        category_id = kwargs['id']
        category_service_details = list(Services.objects.filter(category_id=category_id, is_active=1).values())
        return JsonResponse(category_service_details, safe=False)

class AllUsers(LoginRequiredMixin, View):
    """ List all the Users """

    def get(self, request, *args, **kwargs):
        return JsonResponse(list(User.objects.values()), safe=False )

class ListOffers(LoginRequiredMixin,View):
    """ List all offers """

    def get(self, request, *args, **kwargs):
        list_offers= list(Dealsandoffers.objects.values())
        return JsonResponse(list_offers, safe=False)

class ActiveUsers(LoginRequiredMixin, View):
    """ List active users """

    def get(self, request, *args, **kwargs):
        active_users = list(User.objects.filter(is_active=1).values())
        return JsonResponse(active_users, safe=False)

class AllOrders(LoginRequiredMixin, View):
    """ List active users """

    def get(self, request, *args, **kwargs):
        user_orders = list(User.objects.all().values())
        return JsonResponse(user_orders, safe=False)

class AllCustomers(LoginRequiredMixin, View):
    """ List all customers"""

    def get(self, request, *args, **kwargs):
        list_customer = list(Customer.objects.all().values())
        return JsonResponse(list_customer, safe=False)