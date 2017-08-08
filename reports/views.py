# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from django.contrib.auth.models import User

# Create your views here.

def index(request):
    users = User.objects.all()
    template = loader.get_template('reports/index.html')
    context = {
        'latest_question_list': users,
    }
    return HttpResponse(template.render(context, request))


class IndexView(generic.ListView):
    template_name = 'reports/index.html'
    # template_name = 'reports/static.html'
    context_object_name = 'lists'

    def get_queryset(self):
    	return User.objects.all()


