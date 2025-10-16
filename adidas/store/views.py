from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def shoes(req):
    return HttpResponse("New arrivals")

def men(req):
    return HttpResponse("Men's Footware")

def women(req):
    return HttpResponse("Women's Accessioris")

def kids(req):
    return HttpResponse("Kids wear")