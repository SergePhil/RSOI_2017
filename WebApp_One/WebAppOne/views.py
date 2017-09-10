from django.http import HttpResponse
from django.shortcuts import render


# Create your custom_views here.

def test(request):
    # <view logic>
    return HttpResponse('result')
