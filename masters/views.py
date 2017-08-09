# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from django.views import View
from .forms import MyForm
from django.http import HttpResponseRedirect
import datetime
from django.contrib.auth.models import User
from models import *

# Create your views here.

class Locations_1(generic.ListView):
	"""manage the offiec Locations"""
	template_name = 'locations/index.html'
	context_object_name = 'lists'

	def get_queryset(self):
		return Location.objects.all()


# def create_location(request):
#     if request.method == 'POST':
#         # form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("User created successfully!")
#     else:
#         # form = UserCreationForm()
#         return render(request, 'auth/create_user.html', {'form': form})

class Locations(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'locations/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context_object_name = 'locations'
    	locations = Location.objects.all()
        return render(request, self.template_name, {'locations': locations})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
			# <process form cleaned data>
			time_now = datetime.datetime.utcnow()
			location = Location.objects.create(
			        location_name=form.cleaned_data['location_name'],
			        create_by = 1,
			        updated_date = time_now
			)
			return HttpResponseRedirect('/masters/locations/')

        return render(request, self.template_name, {'form': form})

class CreateLocations2(View):
    model = Location
    fields = ['location_name']
    template_name = 'locations/index.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CreateLocations, self).form_valid(form)     