from django.shortcuts import render

def userModel(request):
    return render(request, "userModel/userModelManage.html")