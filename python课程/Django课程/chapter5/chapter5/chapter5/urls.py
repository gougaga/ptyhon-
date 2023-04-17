#chapter5\chapter5\urls.py
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [ 
    path('test<urlData>', views.showData) ,
    path('admin', admin.site.urls),    
    path('re', views.testHttpResponseRedirect),
    path('rep', views.testHttpResponsePermanentRedirect),
    path('notm', views.testHttpResponseNotModified),
    path('badr', views.testHttpResponseBadRequest),
    path('notf', views.testHttpResponseNotFound),
    path('forb', views.testHttpResponseForbidden),
    path('nota', views.testHttpResponseNotAllowed),
    path('gone', views.testHttpResponseGone),
    path('serror', views.testHttpResponseServerError),
    path('code', views.testStatusCode),
    path('test404', views.testHttp404),
    path('get', views.showGetData),
    path('str/', views.showSomething),
    path('down', views.downloadFile),
    path('csv', views.writecsv),
    path('pdf', views.writepdf),
    path('json', views.writejson),    
    path('uset', views.useTemplateResponse),
    path('redirect', views.useRedirect),
    path('model', views.useModels),
    path('detail/<int:pk>', views.userDetailView.as_view()),
    path('list/', views.userListView.as_view()),
    path('useview', csrf_exempt(views.useClassView.as_view())),
    path('useviewpara', csrf_exempt(views.useClassView.as_view(news='用指定属性值访问视图类'))),
    path('subview', csrf_exempt(views.subClassView.as_view())),
    path('pages', views.useModelsPaginator),
    path('getpng', views.createImg),
    path('getcheck', views.imgCheckCode),
    path('docheck', csrf_exempt(views.verifyCode)),
]
