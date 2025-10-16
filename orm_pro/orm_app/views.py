from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student1
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def get_users(req):
    if req.method =="GET":
        stu_data= Student1.objects.all()
        dict_data=stu_data.values()
        return JsonResponse({"Data":list(dict_data)})
    
    
@csrf_exempt
def reg_user(req):
    if req.method == "POST":
        user_data=json.loads(req.body)
        id=user_data["stu_id"]
        name=user_data["stu_name"]
        branch=user_data["stu_branch"]
        mobile=user_data["stu_mob"]
        
        
        new_student=Student1.objects.create(stu_id=id,stu_name=name,stu_branch=branch,stu_mob=mobile)
        new_student.save()
        return JsonResponse({"msg":"user registerd","data":list(new_student)})
    