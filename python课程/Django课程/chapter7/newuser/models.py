#chapter7\newuser\models.py
from django.db import models
class userinfo(models.Model):
    uid=models.CharField(max_length=10) 
    password=models.CharField(max_length=8) 
    email=models.CharField(max_length=20) 