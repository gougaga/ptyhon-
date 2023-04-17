#chapter5\chapter5\models.py
from django.db import models
class user(models.Model):
    name=models.CharField(max_length=20) 
    age=models.IntegerField()

