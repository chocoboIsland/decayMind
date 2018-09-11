from main_sys import models
import main_sys.templates.DaoTemplate as dao
class Service:

    def __init__(self):
        pass

    #通过id查找
    def findDtoById(self,id):
        pass
    #通过搜索条件查找，结果全返回
    def findDtoBySearchDto(self,dto):
        pass
    #通过搜索条件和页数要求查找，返回查找的页
    def findDtoByPage(self,pageParameter):
        pass

    #
    def findAllDto(self):
        return dao.findAllDto()

    #插入一条数据,dto为json格式
    def insert(self,dto):
        dao.insert(dto)


        #插入多条数据
    def insetList(self,dtoList):
        dao.insetList(dtoList)

    def updateById(self,dto):
        dao.updateById(dto)

    def deleteById(self,id):
        dao.deleteById(id)

    #删除符合搜索条件的所有条目
    def deleteByDto(self,dto):
        dao.deleteByDto(dto)

    #删除所有条目
    def deleteAll(self):
        dao.deleteAll()
