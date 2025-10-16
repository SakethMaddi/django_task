from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
details=[ {
    "id_":1,
    "name":"rakesh",
    "profession":"html"
},{
    "id_":2,
    "name":"kranthi",
    "profession":"js"
},{
    "id_":3,
    "name":"abhishek",
    "profession":"sql"
}] 


@csrf_exempt
def welcome(request):
    if request.method == "GET":
        return HttpResponse("Welcome to GET request")
    elif request.method == "PUT":
        return HttpResponse("Welcome to PUT request")
    elif request.method == "POST":
        return HttpResponse("Welcome to POST request")
    elif request.method == "DELETE":
        return HttpResponse("Welcome to DELETE request")
    elif request.method == "PATCH":
        return HttpResponse("Welcome to PATCH request")
    else: 
        return HttpResponse("invalid request")
    

def details_view(request):
    return JsonResponse({"response":details})

def single_user(request,id):
    for user in details:
        if id==user["id_"]:
            return JsonResponse({"user_data":id})
    return JsonResponse({"msg":"invalid user"})
    
    
@csrf_exempt
def register_user(request):
    # user_data=json.loads(request.body)
    # print(user_data)
    
    print(request.POST.get("id_","profession"))
    print(request.POST.get("name"))
    return HttpResponse("resister app working")
