#chapter5\chapter5\views.py
from django.core.paginator import Paginator
from django.views import View
from datetime import datetime
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from . import models
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from random import randint,choice
from PIL import Image,ImageDraw,ImageFont
from django.http import FileResponse
import csv 
from django.http import Http404,FileResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from django.http import HttpResponseNotModified
from django.http import HttpResponseBadRequest
from django.http import HttpResponseNotFound
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotAllowed
from django.http import HttpResponseGone
from django.http import HttpResponseServerError
from datetime import date

def showData(request,urlData):
    d=date.today()
    s="URL路径中的数据：%s<br>当前日期：%s" %(urlData,d)
    return HttpResponse(s)

def testHttpResponseRedirect(request):
    return HttpResponseRedirect("/admin")

def testHttpResponsePermanentRedirect(request):
    return HttpResponsePermanentRedirect("/admin")

def testHttpResponseNotModified(request):
    return HttpResponseNotModified()

def testHttpResponseBadRequest(request):
    return HttpResponseBadRequest("参数类型错误")

def testHttpResponseNotFound(request):
    return HttpResponseNotFound("未找到请求的内容")

def testHttpResponseForbidden(request):
    return HttpResponseForbidden("禁止访问请求的内容")

def testHttpResponseNotAllowed(request):
    return HttpResponseNotAllowed(['GET',],'不允许使用该方法')

def testHttpResponseGone(request):
    return HttpResponseGone("请求的内容已不存在")

def testHttpResponseServerError(request):
    return HttpResponseServerError("服务器处理出错了")

def testStatusCode(request):
    return HttpResponse(status=401)

def testHttp404(request):
    raise Http404('亲：没有找到你需要的内容!')
    return HttpResponse("ok")

def showGetData(request):
    s='请求上传的数据：姓名=%s，年龄=%s' % (request.GET['name'],request.GET['age'])
    return HttpResponse(s)

def showSomething(request):
    r=HttpResponse('<h1>一级标题</h1>', content_type="text/plain;charset=utf-8")    
    r.write('<p>第二段</p>')
    r.write('three')
    return r

def downloadFile(request):
    r=HttpResponse('文件内容', content_type="text/text;charset=utf-8")
    #r['Content-Disposition'] = 'attachment; filename="test.txt"'
    r.write('\n<h1>test</h1>')
    return r

def writecsv(request):
    r=HttpResponse(content_type="text/text")
    r['Content-Disposition'] = 'attachment; filename="data.csv"'
    w=csv.writer(r)
    w.writerow(['one',1,3,5])
    w.writerow(['two','a''b','5',123])
    return r

def writepdf(request):
    from reportlab.lib.units import cm
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import red
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'
    pdfmetrics.registerFont(TTFont('songti','simsun.ttc')) #注册中文字体，字体文件在当前视图文件目录    
    c = canvas.Canvas(response,pagesize=(10*cm,5*cm))   #生成指定大小的PDF画布
    c.setFont('songti',18)#设置注册的中文字体，以便正常显示汉字
    c.setFillColor(red)#设置颜色
    c.drawString(0.5*cm,4*cm, "Python Django Web简明教程")#在指定位置输出字符串
    c.showPage()#结束当前页面
    c.save()#保存画布
    return response

    from django.http import JsonResponse
def writejson(request):
    #r=HttpResponse(content_type="application/json;charset=utf-8")
    #r.write({'name':'张三','data':[123,'abc']})
    #return r
    
    return JsonResponse({'name':'张三','data':[123,'abc']})



def useTemplateResponse(request):
    return TemplateResponse(request,'info.html',{'name':'张三','age':25})

def useRedirect(request):    
    return redirect(showData,urlData='123')

def useModels(request): 
    uname=request.GET['name']#获取客户端上传的name
    uage=request.GET['age']#获取客户端上传的age
    models.user.objects.create(name=uname,age=uage)     #将数据添加到数据库user表
    s="默认数据库中的user表数据：<br><table><tr><td>id</td><td>name</td><td>age</td></tr>"
    for u in models.user.objects.all():#输出user表全部数据
        s+="<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(u.id,u.name,u.age)
    return HttpResponse(s+'</table>')

def useModelsPaginator(request): 
    objects=models.user.objects.all()       #获取模型全部数据
    pages=Paginator(objects,2)              #创建模型分页器
    page_number = request.GET['page']       #获取请求的页码
    page = pages.get_page(page_number)         #获取指定页面
    list=page.object_list
    s="数据分页显示<hr><table><tr><td>id</td><td>name</td><td>age</td></tr>"
    for u in list:      #输出当前页数据
        s+="<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(u.id,u.name,u.age)
    s+="</table><hr/>"
    if(page.has_previous()):    #创建上一页链接
        s+='<a href="/pages?page=%s">上一页<a/> < '  % page.previous_page_number()
    s+='当前页：%s/%s'  % (page.number,pages.num_pages) #获得当前页码和总页数信息
    if(page.has_next()):        #创建下一页链接
        s+=' > <a href="/pages?page=%s">下一页<a/>'  % page.next_page_number()
    return HttpResponse(s)


class useClassView(View):    
    news="使用基于类的视图useClassView"
    form='<form name="input" action="" method="post">' \
                +'请输入数据: <input type="text" name="data">' \
                +'<input type="submit" value="提交"></form> '
    def get(self, request):             #响应HTTP GET请求
        out=self.news+'<br/>请求方法：GET<br/>'+self.form        
        return HttpResponse(out)   #返回响应    
    def post(self, request):            #响应HTTP POST请求
        out=self.news+'<br/>请求方法：POST<br/>' \
            +'上传的数据为：'+request.POST['data']+self.form        
        return HttpResponse(out)   #返回响应

class subClassView(useClassView):    
    news="这是视图类useClassView的扩展类！"    
    def get(self, request):             #重载get()方法
        out=self.news+'<br/>重载get()方法输出：请在输入数据后提交！<br/>'+self.form        
        return HttpResponse(out)           
   

class userDetailView(DetailView):
    model = models.user             #指定模型
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.now()     #向上下文添加额外数据
        return context

class userListView(ListView):
    model = models.user         #指定模型
    
def getRandomColor():       #获取随机颜色
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def getRandomChar():        #获取随机字符
    num =str(randint(0,9))       
    lower=chr(randint(97,122))
    upper=chr(randint(65,90))
    char=choice([num,lower,upper])
    return char

def createImg(request):    #创建验证码图片返回
    img=Image.new(mode="RGB",size=(160,30),color=(100,100,100))    #创建图片
    draw=ImageDraw.Draw(img)    #获取图片画笔，用于描绘字
    font=ImageFont.truetype(font="arial.ttf",size=24) #设置字体，字体文件和视图文件放在同一个文件夹中
    code=''
    for i in range(5):             
        c=getRandomChar()                   #获得随机字符
        draw.text((10+30*i,2),text=c,fill=(255,255,255),font=font)#根据坐标填充文字
        code+=c                             #记录验证码字符
    request.session['randomcode']=code      #将验证码存入session
    f=open("test.png",'wb')
    img.save(f, format="png")
    f.close()
    return FileResponse(open("test.png",'rb'))

def verifyCode(request):        #验证用户提交的验证码是否正确
    out="验证码不正确！"
    if request.POST['code'].upper()==request.session['randomcode'].upper():
        out="验证码正确！"
    return HttpResponse(out)

def imgCheckCode(request):
    form='<form name="input" action="/docheck" method="post">'\
                +'<a href="/getcheck"><img src="/getpng"></a>单击图片刷新<br>' \
                +'请输入图中的校验码: <input type="text" name="code" maxlength=5 size=8>' \
                +'<input type="submit" value="提交"></form> '
    return HttpResponse(form)

