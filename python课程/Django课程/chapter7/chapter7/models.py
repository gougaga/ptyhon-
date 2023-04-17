#chapter7\chapter7\models.py
from django.db import models
class person(models.Model):
    name=models.CharField(max_length=8) 
    age=models.SmallIntegerField()
