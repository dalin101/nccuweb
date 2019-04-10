from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import auth  
from django.contrib.auth.forms import UserCreationForm 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def toLogin(request):
	return render(request,'login.html')

def toRegister(request):
	return render(request,'register.html')

def toProfile(request):
	return render(request,'profile.html')

def toBranchInfo(request):
	return render(request,'branch.html')

def toProductInfo(request):
	return render(request,'product.html')

# login
@csrf_exempt
def login(request):

    if request.user.is_authenticated(): 
        return JsonResponse({"status": True})

    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        print("success")
        return JsonResponse({"status": True})
    else:
        print(password)
        print("fail")
        return JsonResponse({"status": False})
