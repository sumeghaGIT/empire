# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login/')
def index(request):
    users = User.objects.all()
    template = loader.get_template('reports/index.html')
    context = {
        'latest_question_list': users,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
def indexView(request):
    user = User.objects.all()
    return render(request, 'reports/static.html', {'user':user})



