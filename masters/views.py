# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.views import View
from masters.forms import LocationsForm, CategoriesForm, ServicesForm
from django.http import HttpResponseRedirect
import datetime
from django.contrib.auth.models import User
from masters.models import *

# Create your views here.

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
        services = Services.objects.all()
        return render(request, self.template_name, {'services':services,'form':form})

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

class CreateServices(View):
    form_class = ServicesForm
    initial = {'service_name': ''}
    template_name = 'services/add.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
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