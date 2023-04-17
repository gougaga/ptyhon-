#chapter6\chapter6\views.py
from django.core.paginator import Paginator
from django.shortcuts import render
from . import models

from django.http import HttpResponse
from datetime import datetime
from django.template.loader import get_template
from django.template.response import TemplateResponse
def getTime(request):
    time=datetime.today()    
    t=get_template('mytemplate.html')
    html=t.render({'time':time})
    return HttpResponse(html)
    
def getTime2(request):
    time=datetime.today()          
    return TemplateResponse(request,'mytemplate.html',{'time':time})

def getTime3(request):
    time=datetime.today()          
    return render(request,'mytemplate.html',{'time':time})
class user:pass

def testTemplate(request):
    return render(request,'stemplate.html')

def useTempaltePaginator(request): 
    objects=models.score.objects.all()       				#获取全部成绩数据
    pages=Paginator(objects,10)              			#创建分页器，每页10条记录
    page_number = request.GET['page']       			#获取请求的页码
    page = pages.get_page(page_number)         		#获取指定页面
    return render(request, 'pagetemplate.html', {'scores': page})
