"""chapter8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from dingding.test import views as log_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',log_views.login_ok),
    path('test/login/', auth_views.LoginView.as_view(template_name='test/login.html')),
    path('test/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out2.html'),name='logout2'),
    path('test/logindiy/', log_views.login_diy,name='logindiy'),
    path('test/logindiy_success/', log_views.log_success,name='log_success'),
    path('test/logoutdiy/', log_views.logout_diy,name='logoutdiy'),
    path('test/testlog/', log_views.testlogin,name='testlogin'),
    path('test/testlog2/', log_views.testlogin2,name='testlogin2'),
    path('test/testlog3/', log_views.testlogin3,name='testlogin3'),
    path('test/testlog4/', log_views.testlogin4,name='testlogin4'),
    path('sendemail/', log_views.sendEmail),
    path('setcolor/', log_views.setcolor,name='setcolor'),
    path('usecolor/', log_views.usecolor,name='usecolor'),
]