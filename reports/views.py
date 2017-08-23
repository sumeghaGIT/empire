# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


from masters import models

User = get_user_model()


@login_required(login_url='/accounts/login/')
def indexView(request):
    user = User.objects.all()
    return render(request, 'reports/static.html', {"user": user})


def ticketView(request):

    return render(request, 'reports/create_ticket.html')


def notification(request):
    notification_obj = models.Ticket.objects.filter(is_active='Y')
    notification = []
    notification_count = notification_obj.count()
    return JsonResponse({'notification_count': notification_count})