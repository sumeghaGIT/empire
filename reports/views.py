# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required(login_url='/accounts/login/')
def indexView(request):
    user = User.objects.all()

    return render(request, 'reports/static.html', {'user': user})


def ticketView(request):

    return render(request, 'reports/create_ticket.html')
