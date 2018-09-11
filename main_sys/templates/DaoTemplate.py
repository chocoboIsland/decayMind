from main_sys import models

#通过id查找
def findDtoById(id):
    pass

#通过搜索条件查找，结果全返回
def findDtoBySearchDto(dto):
    pass
#通过搜索条件和页数要求查找，返回查找的页
def findDtoByPage(pageParameter):
    pass

#
def findAllDto():
    return models.UserInfo.objects.all()

#插入一条数据,dto为json格式
def insert(dto):
    models.UserInfo.objects.create(**dto)

    #插入多条数据
def insetList(dtoList):
    for item in dtoList:
        models.UserInfo.objects.create(**item)
    pass

def updateById(dto):
    models.UserInfo.objects.filter(id=dto[id]).update(**dto)

def deleteById(deleteId):
    models.UserInfo.objects.filter(id=deleteId).delete()

#删除符合搜索条件的所有条目
def deleteByDto(dto):
    models.UserInfo.objects.filter(**dto).delete()

#删除所有条目
def deleteAll():
    models.UserInfo.objects.all().delete()

