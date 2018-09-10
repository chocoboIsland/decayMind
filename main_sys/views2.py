from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html",)

def playground(request):
    return render(request,"test.html")

def userModel(request):
    return render(request, "userModel/userModelManage.html")
