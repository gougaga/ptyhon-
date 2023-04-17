#chapter6\chapter6\models.py
from django.db import models
class score(models.Model):
    kh=models.CharField(max_length=8) #考号
    xm=models.CharField(max_length=8) #姓名
    yw=models.IntegerField()#语文成绩
    sx=models.IntegerField()#数学成绩
    yy=models.IntegerField()#英语成绩
