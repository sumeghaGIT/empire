# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views import View


from masters import models
from masters.forms import LocationsForm, CategoriesForm, ServicesForm, CreateUserForm, TaskStatusForm


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
            # <process form cleaned data>
            time_now = datetime.datetime.utcnow()
            location = models.Location.objects.create(
                    name=form.cleaned_data['location_name'],
                    is_active= form.cleaned_data['status'],
                    created_by=request.user.id,
                    updated_date=time_now
            )
            return HttpResponseRedirect('/masters/locations/')
        return render(request, self.template_name, {'form': form})

class DeleteLocations(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        # if 'pk' in kwargs and kwargs['pk'] is not None:
        # print "ddddddddddddddddddddddddddddddddddddddd",kwargs['id']
        b = models.Location.objects.get(id=2)
        b.delete()
        return 'True'

class RequestDeleteView(LoginRequiredMixin, DeleteView):
    """
    Sub-class the DeleteView to restrict a User from deleting other 
    user's data.
    """
    template_name = 'locations/index.html'
    success_message = "Deleted Successfully"
    model = models.Location
    success_url = "masters/locations/"

    def get_queryset(self, **kwargs):
        qs = super(RequestDeleteView, self).get_queryset()
        # return qs.filter(id=self.request.user)
        return qs.filter(id=2)


class CategoriesLists(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = CategoriesForm
    initial = {'location_name': ''}
    template_name = 'categories/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        categories = models.Categories.objects.all()
        return render(request, self.template_name, {'categories':categories,'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            time_now = datetime.datetime.utcnow()
            location = models.Categories.objects.create(
                    name=form.cleaned_data['category_name'],
                    created_by=request.user.id,
                    updated_by=request.user.id,
                    is_active= form.cleaned_data['status']
            )
            return HttpResponseRedirect('/masters/categories/')
        return render(request, self.template_name, {'form': form})


class ServicesLists(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = ServicesForm
    initial = {'location_name': ''}
    template_name = 'services/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        # services = Services.objects.select_related('category').filter(is_active=1).order_by('-pk')
        services = models.Services.objects.select_related('category').all().order_by('-pk')
        return render(request, self.template_name, {'services':services,'form':form})


class CreateServices(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    form_class = ServicesForm
    initial = {'service_name': ''}
    template_name = 'services/add.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            time_now = datetime.datetime.utcnow()
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
                    updated_date=time_now
            )
            return HttpResponseRedirect('/masters/services/')
        return render(request, self.template_name, {'form': form})

class UpdateServices_main(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    model = models.Services
    fields = ['name','response_time','threshold_time','category']
    template_name = 'services/edit.html'

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
            # <process form cleaned data>
            time_now = datetime.datetime.utcnow()
            if 'pk' in kwargs and kwargs['pk'] is not None:
                services = models.Services.objects.get(id=kwargs['pk'])
                services.name = form.cleaned_data['service_name']
                services.category_id=int(form.cleaned_data['category_name'].id)
                services.response_time=form.cleaned_data['response_time']
                services.threshold_time=form.cleaned_data['threshold_time']
                services.price=form.cleaned_data['price']
                services.service_from=form.cleaned_data['service_from']
                services.service_to=form.cleaned_data['service_to']
                services.is_active=form.cleaned_data['status']
                services.updated_by=request.user.id
                services.updated_date=time_now
                services.save()

            return HttpResponseRedirect('/masters/services/edit/'+kwargs['pk']+'/')
        return render(request, self.template_name, {'form': form})

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
            # <process form cleaned data>
            time_now = datetime.datetime.utcnow()
            location = models.TaskStatus.objects.create(
                    status=form.cleaned_data['name'],
                    created_by=request.user.id,
                    updated_by=request.user.id,
                    is_active= form.cleaned_data['status'],
            )
            return HttpResponseRedirect('/masters/tasks/')
        return render(request, self.template_name, {'form': form})

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
            # <process form cleaned data>
            time_now = datetime.datetime.utcnow()
            location = models.InquiryStatus.objects.create(
                    status=form.cleaned_data['name'],
                    created_by=request.user.id,
                    updated_by=request.user.id,
                    is_active= form.cleaned_data['status'],
            )
            return HttpResponseRedirect('/masters/inquiry/')
        return render(request, self.template_name, {'form': form})

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
            # <process form cleaned data>
            time_now = datetime.datetime.utcnow()
            location = models.InquirySources.objects.create(
                    sources=form.cleaned_data['name'],
                    created_by=request.user.id,
                    updated_by=request.user.id,
                    is_active= form.cleaned_data['status'],
            )
            return HttpResponseRedirect('/masters/inquiry/sources/')
        return render(request, self.template_name, {'form': form})

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
            # <process form cleaned data>
            time_now = datetime.datetime.utcnow()
            location = models.Department.objects.create(
                    name=form.cleaned_data['name'],
                    created_by=request.user.id,
                    updated_by=request.user.id,
                    is_active= form.cleaned_data['status'],
            )
            return HttpResponseRedirect('/masters/departments/')
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
