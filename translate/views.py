import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse('Welcome to translate ')
    elif request.method == 'POST':
        # print(f"{request.body}")
        json_data = json.loads(request.body)
        return HttpResponse(f"{json_data}")
