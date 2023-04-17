from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from chapter8 import settings
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.decorators import user_passes_test

def login_ok(request):    
    return render(request,'login_ok.html')

def login_diy(request):  
    uid = ''
    news=''
    if request.method == 'POST':
        uid = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uid, password=pwd)
        if user is not None:
            login(request, user)        #执行登录操作
            return redirect('log_success')#重定向
        else:
            news="用户名或密码错误！"     
    context={'username':uid, 'news':news}
    return  render(request, 'login_diy.html', context)

def log_success(request):
    news='登录成功，欢迎：%s，<a href="%s">注销登录？</a>'%\
        (request.user.username,reverse('logoutdiy'))
    return HttpResponse(news)

def logout_diy(request):
    logout(request) #注销登录
    news='登录注销成功，欢迎<a href="%s">再次登录？</a>'%reverse('logindiy')
    return HttpResponse(news)

def testlogin(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        news='欢迎：%s，你已经登录，可以访问本页面，<a href="%s">注销登录？</a>'%\
        (request.user.username,reverse('logoutdiy'))
        return HttpResponse(news)

@login_required
def testlogin2(request):
    news='欢迎：%s，你已经登录，可以访问本页面，<a href="%s">注销登录？</a>'%\
    (request.user.username,reverse('logoutdiy'))
    return HttpResponse(news)

@login_required
@permission_required('test.can_testlog')
def testlogin3(request):
    news='欢迎：%s，你已经登录，可以访问本页面，<a href="%s">注销登录？</a>'%\
    (request.user.username,reverse('logoutdiy'))
    return HttpResponse(news)

def check_in_blacklist(user):#检测用户是否在黑名单中
    return not user.username in settings.LOGIN_BLACKLIST
@user_passes_test(check_in_blacklist)
def testlogin4(request):
    news='欢迎：%s，你已经登录，可以访问本页面，<a href="%s">注销登录？</a>'%\
    (request.user.username,reverse('logoutdiy'))
    return HttpResponse(news)

from django import forms
from django.core.validators import validate_email
class MultiRecipientField(forms.CharField):#自定义多个收件人字段
    def to_python(self, value):     #将分号分隔的多个收件人转换为列表     
        if not value:
            return []
        return value.split(';')     
    def validate(self, value):      
        super().validate(value)
        for email in value:
            validate_email(email)   #验证每个收件人地址是否有效
class emailForm(forms.Form):
    subject = forms.CharField(label='主题')
    from_email = forms.EmailField(label='发件人',initial=settings.EMAIL_HOST_USER)
    to_email = MultiRecipientField(label='收件人')  
    message = forms.CharField(label='内容',widget=forms.Textarea)

from django.core.mail import send_mail
def sendEmail(request):    
    msg=''
    if request.method == 'POST':            #处理表单提交的邮件内容
        form = emailForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            from_email=form.cleaned_data['from_email']
            to_email=form.cleaned_data['to_email']
            message=form.cleaned_data['message']
            send_mail(subject,message,from_email,to_email,fail_silently=False)
            form = emailForm()    
            msg='已成功发送邮件！'
    else:
        form = emailForm()
    return render(request, 'sendemail.html', {'form': form,'msg':msg})

def setcolor(request):  
    if request.method == 'POST':
        color=request.POST.get('color')
        request.session['bgcolor']=color                #将颜色存入Session
        return redirect('usecolor')
    return render(request, 'selectcolor.html')

def usecolor(request):  
    color=request.session.get('bgcolor',False)              #获取Session中的颜色
    if not color:
        return redirect('setcolor')
    return render(request, 'usecolor.html',{'bgcolor':color})