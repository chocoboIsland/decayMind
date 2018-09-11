class PageParameter():
    def __init__(self,page,row):
        self.page=page#当前第几页
        self.rows=row#每页多少记录

    #总页数
    def setTotalPage(self,totalPage):
        self.totalPage=totalPage

    def getTotalPage(self):
        return self.totalPage

    #总记录数
    def setTotalRows(self,totalRows):
        self.totalRows=totalRows

    def getTotalRows(self):
        return self.totalRows