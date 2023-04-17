#chapter6\chapter6\urls.py
from django.urls import path
from chapter6 import views
urlpatterns = [
    path('time', views.getTime),
    path('time2', views.getTime2),
    path('time3', views.getTime3),
    path('test', views.testTemplate),
    path('scores', views.useTempaltePaginator),
]
