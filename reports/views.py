# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.models import User

# Create your views here.

def index(request):
    latest_question_list = [{'id':1,'question_text':'question of maths'},
    {'id':2,'question_text':'question of Physics'},{'id':3,'question_text':'question Chemistry'},]
    users = User.objects.all()
    template = loader.get_template('reports/index.html')
    context = {
        'latest_question_list': users,
    }
    return HttpResponse(template.render(context, request))

