#chapter7\chapter7\urls.py
from django.urls import path
from . import views
from newuser import views as newuser_views
urlpatterns = [
    path('getdata/', views.getdata),
    path('dform/', views.useDataForm),
    path('dform3/', views.useDataForm3),
    path('diyfield/', views.useTest),
    path('diyfor/', views.useTestFor),
    path('formset/', views.useFormset),
    path('mform/', views.usePersonForm),
    path('mdiy/', views.usePersonFormDIY),
    path('media/', views.usePersonFormDIY_Media),
    path('first/', views.getinfofirst),
    path('getinfo/', views.getPersopnInfo),
    path('getpng/', newuser_views.createImg), 
    path('checkuid/', newuser_views.doCheckUid), 
    path('checkcode/', newuser_views.returnCheckCode), 
    path('newfirst/', newuser_views.toAddNew),
    path('addnew/', newuser_views.doAddNew),
]
