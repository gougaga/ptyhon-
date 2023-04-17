#chapter7\chapter7\views.py
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.forms import ModelForm,ValidationError
from .models import person
from django.forms import formset_factory
from django import forms
from django.shortcuts import render
from datetime import datetime

def getdata(request):
    data=''
    if 'data' in request.POST:
        data=request.POST['data']   #获取客户端提交的data
    return render(request,'temform.html',{'current_data':data})

class dataForm(forms.Form):
    data = forms.CharField(label='请输入数据',)

def useDataForm(request):
    if request.method == 'POST':        
        form = dataForm(request.POST)  #使用接收到的数据创建表单
        msg="已完成数据提交！"
    else:
        form = dataForm()#创建空白表单
        msg='初始表单'
    return render(request, 'temdataform.html', {'form': form,'msg':msg})

def useDataForm3(request):    
    return render(request, 'temdataform3.html', {'form': dataForm()})

class test(forms.Form):
    name=forms.CharField(max_length=50,label='姓名')
    age=forms.IntegerField(max_value=50,min_value=15,\
                 label='年龄',help_text='年龄不小于15且不大于50')
def useTest(request):
    if request.method == 'POST':        
        form = test(request.POST)        
    else:
        form = test()
    return render(request, 'temtest.html', {'form': form})

def useTestFor(request):
    return render(request, 'temtestfor.html', {'form': test()})

def useFormset(request):
    classTestFormset=formset_factory(test,extra=2)  #创建表单集类
    if request.method == 'POST':        
        formset = classTestFormset(request.POST)        
    else:
        formset = classTestFormset()
    return render(request, 'temformset.html', {'formset': formset})

class personForm(ModelForm):
    class Meta:
        model = person      #指定模型
        fields = '__all__'  #指定字段

def usePersonForm(request):    
    if request.method == 'POST':      #在提交表单时采用POST方法  
        mform = personForm(request.POST)#用提交的方法初始化表单
        if mform.is_valid():#在表单通过验证时执行数据处理
            ps=person.objects.filter(name=request.POST['name'])#用表单数据查询
            if ps.count()==0:
                mform.save()#不存在相同姓名时，将数据存入数据库
                msg='数据已保存！'
            else:
                msg='数据库已存在相同姓名的数据，请勿重复提交！'
        else:msg='表单数据有错'
    else:
        mform = personForm()#创建空白表单
        msg="请输入数据添加新记录"
    return render(request, 'temmodelform.html', {'mform': mform,'msg':msg})

def validate_age(value):
  if int(value) < 20:
      raise ValidationError('年龄不能小于20！',code='min_value')
  elif int(value) > 50:
      raise ValidationError('年龄不能大于50！',code='max_value')

class personFormDIY(ModelForm):
    #重定义age字段
    age=forms.CharField(validators=[validate_age],label='年龄',\
                        widget = forms.NumberInput(),\
                        help_text = '年龄为[20,50]以内的整数')
    class Meta:
        model = person              #指定模型
        fields = ['name', 'age']    #指定字段
        labels = { 'name': '姓名',}   #设置字段渲染后的<label>内容
        help_texts = {'name':'姓名为中英文字符串',}#设置字段帮助文本
        widgets = {'name': forms.Textarea(attrs={'cols': 30, 'rows': 2}),}

def usePersonFormDIY(request):    
    if request.method == 'POST':  
        mform = personFormDIY(request.POST)
        if mform.is_valid():
            ps=person.objects.filter(name=request.POST['name'])
            if ps.count()==0:
                mform.save()
                msg='数据已保存！'
            else:
                msg='数据库已存在相同姓名的数据，请勿重复提交！'     
        else:msg='表单数据有错'
    else:
        mform = personFormDIY()
        msg="请输入数据添加新记录"
    return render(request, 'temmodelformdiy.html', {'mform': mform,'msg':msg})

class personFormDIY_Media(ModelForm):
    #重定义age字段
    age=forms.CharField(validators=[validate_age],label='年龄',\
                        widget = forms.NumberInput(),\
                        help_text = '年龄为[20,50]以内的整数')
    class Meta:
        model = person              #指定模型
        fields = ['name', 'age']    #指定字段
        labels = { 'name': '姓名',}   #设置字段渲染后的<label>内容
        help_texts = {'name':'姓名为中英文字符串',}#设置字段帮助文本
        widgets = {'name': forms.Textarea(attrs={'cols': 30, 'rows': 2}),}
    class Media:
        css={'all': ('/static/diyform.css',)}
        js = ('/static/focusinput.js',)

def usePersonFormDIY_Media(request):    
    if request.method == 'POST':  
        mform = personFormDIY_Media(request.POST)
        if mform.is_valid():
            ps=person.objects.filter(name=request.POST['name'])
            if ps.count()==0:
                mform.save()
                msg='数据已保存！'
            else:
                msg='数据库已存在相同姓名的数据，请勿重复提交！'     
        else:msg='表单数据有错'
    else:
        mform = personFormDIY_Media()
        msg="请输入数据添加新记录"
    return render(request, 'temmedia.html', {'mform': mform,'msg':msg})

def getinfofirst(request):
    return TemplateResponse(request,'temajax.html')
def getPersopnInfo(request):    
    ps=person.objects.filter(name__startswith=request.GET['name'])
    if ps.count()>0:            
        result='姓名以“%s”开始的用户信息：<br><table>'%request.GET['name']
        n=0
        for a in ps:
            n+=1
            result+="<tr><td>%s</td><td>%s</td><td>%s</td></tr>" %(n,a.name,a.age)
        result+='</table>'
    else:
        result='没有匹配的用户信息！'
    return HttpResponse(result)  