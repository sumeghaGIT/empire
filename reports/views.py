# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View


@login_required(login_url='/accounts/login/')
def indexView(request):
    user = User.objects.all()
    return render(request, 'reports/static.html', {'user': user})


class TicketView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'reports/create_ticket.html')
