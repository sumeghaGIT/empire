# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.views.generic.edit import CreateView
from django.views import View
from masters.forms import LocationsForm, CategoriesForm, ServicesForm, CreateUserForm
from django.http import HttpResponseRedirect
import datetime
from django.contrib.auth.models import User
from masters.models import *
from django.shortcuts import render, redirect

class Locations(View):
    form_class = LocationsForm
    initial = {'location_name': ''}
    template_name = 'locations/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        locations = Location.objects.all()
        return render(request, self.template_name, {'locations':locations,'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
			# <process form cleaned data>
			time_now = datetime.datetime.utcnow()
			location = Location.objects.create(
			        name=form.cleaned_data['location_name'],
			        created_by = request.user.id,
			        updated_date = time_now
			)
			return HttpResponseRedirect('/masters/locations/')

        return render(request, self.template_name, {'form': form})

class CategoriesLists(View):
    form_class = CategoriesForm
    initial = {'location_name': ''}
    template_name = 'categories/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        categories = Categories.objects.all()
        return render(request, self.template_name, {'categories':categories,'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            time_now = datetime.datetime.utcnow()
            location = Categories.objects.create(
                    name=form.cleaned_data['category_name'],
                    created_by = request.user.id,
                    updated_by = request.user.id
                    # updated_date = time_now
            )
            return HttpResponseRedirect('/masters/categories/')

        return render(request, self.template_name, {'form': form})


class ServicesLists(View):
    form_class = CategoriesForm
    initial = {'location_name': ''}
    template_name = 'services/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        # services = Services.objects.select_related('category').filter(is_active=1).order_by('-pk')
        services = Services.objects.select_related('category').all().order_by('-pk')
        return render(request, self.template_name, {'services':services,'form':form})

class CreateServices(View):
    form_class = ServicesForm
    initial = {'service_name': ''}
    template_name = 'services/add.html'

    def get(self, request, *args, **kwargs):
        data = {}
        if 'id' in kwargs and kwargs['id'] is not None:
            services = Services.objects.get(id=kwargs['id'])
            data = {'service_name':services.name,'response_time':services.response_time,'threshold_time':services.threshold_time,'category_name':services.category_id}
        form = self.form_class(initial=data)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            time_now = datetime.datetime.utcnow()
            services = Services.objects.create(
                    name=form.cleaned_data['service_name'],
                    category_id=int(form.cleaned_data['category_name'].id),
                    response_time=form.cleaned_data['response_time'],
                    threshold_time=form.cleaned_data['threshold_time'],
                    created_by = request.user.id,
                    updated_by = request.user.id,
                    updated_date = time_now
            )
            return HttpResponseRedirect('/masters/services/')

        return render(request, self.template_name, {'form': form})

from django.views.generic.edit import CreateView, UpdateView, DeleteView
class UpdateServices(UpdateView):
    model = Services
    # form_class = ServicesForm
    fields = ['name','response_time','threshold_time','category']
    template_name = 'services/edit.html'
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ServicesForm, self).form_valid(form)

class CreateUser(View):

    def get(self, request, *args, **kwargs):
        form = CreateUserForm()
        return render(request, 'allauth/templates/account/create.html', {'form':form})

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
            return render(request, 'allauth/templates/account/create.html', {'form':form})


class ManageUser(View):

    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        return render(request, 'allauth/templates/account/manageuser.html', {'users':user})
