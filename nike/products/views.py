from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cart(req):
    return HttpResponse("Welcome to the cart")

def models(req):
    return HttpResponse("Welcome to Nike models")

def men(req):
    return HttpResponse("Men's Section")

def women(req):
    return HttpResponse("Women's Section")