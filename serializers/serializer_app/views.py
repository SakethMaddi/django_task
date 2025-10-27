from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
import json
from .models import Coders
from .serializer import CoderSerializer

# Create your views here.
def get_users(req):
    
    # coders_data=Coders.objects.all()
    # dist_data=coders_data.values()
    # return JsonResponse({"Coders":list(dist_data)})

    data=Coders.objects.all()
    all_users=CoderSerializer(data,many=True)
    return JsonResponse({"coders":all_users.data})


@csrf_exempt
def update_users(req,id):
    user=Coders.objects.get(c_id=id)
    user_data=json.loads(req.body)
    serializer=CoderSerializer(user, data=user_data ,partial=True)
    if serializer.is_valid():
        serializer.save()
        return HttpResponse("User updated")
    else: 
         return HttpResponse("invalid data")

@csrf_exempt
def delete_users(req,id):
    try:
        existing_c=Coders.objects.get(c_id=id)
    except:
        return HttpResponse("user not found")
    
    existing_c.delete()
    return HttpResponse("user deleted")


@csrf_exempt
def reg_users(req):
    coder_id=req.POST.get("id")
    coder_name=req.POST.get("name")
    coder_phone=req.POST.get("phone")
    coder_email=req.POST.get("email")
    
    coder= Coders.objects.create(id=coder_id,name=coder_name,phone=coder_phone,email=coder_email)
    coder.save()
    return HttpResponse("registered")