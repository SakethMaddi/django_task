from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
import json

# Create your views here.

@csrf_exempt
def users(req):
    emp_data=Employee.objects.all()
    dict_data=emp_data.values()
    return JsonResponse({"data":list(dict_data)})
    
    
    
    # first_name=req.POST.get("fname")
    # last_name=req.POST.get("lname")
    # salary=int(req.POST.get("salary"))
    # department=req.POST.get("dept")
    # emp_id=int(req.POST.get("emp_id"))
    
    # employee=Employee.objects.create(first_name=first_name,last_name=last_name,salary=salary,department=department,emp_id=emp_id)
    # employee.save()
    # return HttpResponse("welcome")
