from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from jinja2 import Environment, PackageLoader, FileSystemLoader, ChoiceLoader
import main_sys.templates.ServiceTemplate as service

def userModel(request):
    loader = ChoiceLoader([
        FileSystemLoader(settings.TEMPLATE_DIRS),
        PackageLoader('main_sys', 'templates')
    ])
    env = Environment(loader=loader)
    template = env.get_template('viewTemplate.html')
    showfields=["字段1","字段2","字段3"]
    userService=service.Service()
    listDto=[{'username':'name2',"password":'123456','accountMoney':1239.0 },
             {'username': 'name3', "password": '123456', 'accountMoney': 1239.0},
             {'username': 'name4', "password": '123456', 'accountMoney': 1239.0}]
    uDto={'id':'6','username':'name2',"password":'112232','accountMoney':1221.0 }
    #userService.insetList(listDto)
    userService.updateById(uDto)

    allList=userService.findAllDto()
    print(allList)
    return HttpResponse(
        template.render(fields=showfields,values=allList)
    )
    #return render(request, "userModel/userModelManage.html")