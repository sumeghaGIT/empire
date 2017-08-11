# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.views import View


from masters import models

"""
@login_required(login_url='/accounts/login/')
def indexView(request):
    user = User.objects.all()
    return render(request, 'reports/static.html', {'user': user})


class TicketView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'reports/create_ticket.html')

    def post(self, request):
        ticket_type = request.POST.get('ticket_type')
        if ticket_type == 'query':
            query = request.POST.get('query_text')
            notification = models.Notifications.objects.create(notification=query,
                                                               created_by=request.user.id,
                                                               updated_by=request.user.id)
            notification.save()
            return HttpResponse("ticket created successfully")
"""