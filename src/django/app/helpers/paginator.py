from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PaginatorHelper:
    def __init__(self,dict,cant):
        self.dict = dict
        self.cant = cant

    def getPage(self,page):
        if self.dict and len(self.dict) > 0:
            paginator = Paginator(self.dict,self.cant)
            try:
                pagedDict = paginator.page(page)
            except PageNotAnInteger:
                pagedDict = paginator.page(1)
            except EmptyPage:
                pagedDict = paginator.page(paginator.num_pages)
            return pagedDict
        else:
            return []
