from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Workers


def index(request):
    workers_list = Workers.objects.order_by('id')[:5]
    output = ', '.join([q.name for q in workers_list])
    return HttpResponse(output)