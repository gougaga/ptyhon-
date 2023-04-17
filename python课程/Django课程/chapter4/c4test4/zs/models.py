from django.db import models
class zy(models.Model):
    zsdm=models.PositiveSmallIntegerField(primary_key=True)
    zymc=models.CharField(max_length=10)
    cc=models.CharField(max_length=10)
    sfbz=models.PositiveSmallIntegerField()
class lq(models.Model):
    zkzh=models.CharField(max_length=9,primary_key=True)
    xm=models.CharField(max_length=10)
    zy=models.ForeignKey(zy,null=True,on_delete=models.CASCADE)