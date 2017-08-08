# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from models import *

# Create your views here.

class Locations(generic.ListView):
	"""manage the offiec Locations"""
	template_name = 'locations/index.html'
	context_object_name = 'lists'

	def get_queryset(self):
		return User.objects.all()


class CreateLocations22(generic.ListView):
	"""manage the offiec Locations"""
	template_name = 'locations/create.html'
	context_object_name = 'lists'

	def get_queryset(self):
		return User.objects.all()

# def create_location(request):
#     if request.method == 'POST':
#         # form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("User created successfully!")
#     else:
#         # form = UserCreationForm()
#         return render(request, 'auth/create_user.html', {'form': form})

class CreateLocations(CreateView):
    model = Location
    fields = ['location_name']
    template_name = 'locations/create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        print ">>>>>>>>>",self.request 
        return super(CreateLocations, self).form_valid(form)     