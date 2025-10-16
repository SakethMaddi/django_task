from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def reg_user(request):
    first_name=request.POST.get("fname"),
    last_name=request.POST.get("lname"),
    age=request.POST.get("age"),
    roll_number=request.POST.get("rnum"),

    Student1=Student.objects.create(first_name=first_name,last_name=last_name,age=age,roll_number=roll_number)
    Student1.save()
    
    return HttpResponse("welcome")

