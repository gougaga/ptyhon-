# chapter4\faqs\models.py
from django.db import models


class faqsdata(models.Model):
    question = models.CharField(max_length=200, blank=True)
    answer = models.CharField(max_length=200, blank=True)


class test1(models.Model):
    field1 = models.CharField(max_length=200, db_index=True)  # 为字段创建普通索引
    field2 = models.CharField(max_length=200, unique=True)  # 为字段创建唯一索引


class test2(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)

    class Meta:
        indexes = [models.Index(fields=['field1'], name='idx_field1')]  # 定义索引


class test3(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)

    class Meta:
        unique_together = ('field1', 'field2')  # 创建组合唯一索引


class scores(models.Model):  # 定义实例数据模型，id字段自动添加，无需定义
    kh = models.CharField(max_length=8)
    xm = models.CharField(max_length=8)
    yw = models.SmallIntegerField()
    sx = models.SmallIntegerField()
    bj = models.CharField(max_length=8)


class banj(models.Model):  # 班级模型
    mc = models.CharField(max_length=8)  # 班级名称

    def __str__(self):
        return self.mc


class xues(models.Model):  # 学生模型
    xm = models.CharField(max_length=8)  # 学生姓名
    bj = models.ForeignKey(banj, on_delete=models.CASCADE, null=True)  # 外键，关联班级

    def __str__(self):
        return self.xm


class shet(models.Model):  # 社团模型
    mc = models.CharField(max_length=8)  # 社团名称

    def __str__(self):
        return self.mc


class stus(models.Model):  # 学生模型
    xm = models.CharField(max_length=8)  # 学生姓名
    shets = models.ManyToManyField(shet)  # 外键，关联社团

    def __str__(self):
        return self.xm


class shet2(models.Model):  # 社团模型2
    mc = models.CharField(max_length=8)  # 社团名称

    def __str__(self):
        return self.mc


class stus2(models.Model):  # 学生模型2
    xm = models.CharField(max_length=8)  # 学生姓名
    shets = models.ManyToManyField(shet2, through='ssRelations')  # 外键，关联中间模型

    def __str__(self):
        return self.xm


class ssRelations(models.Model):  # 中间模型
    st = models.ForeignKey(shet2, on_delete=models.CASCADE, null=True)  # 外键，关联社团模型2
    stu = models.ForeignKey(stus2, on_delete=models.CASCADE, null=True)  # 外键，关联学生模型2
    jdate = models.DateField()  # 加入社团日期


class stus3(models.Model):  # 学生模型3
    xm = models.CharField(max_length=8)  # 学生姓名

    def __str__(self):
        return self.xm


class cards(models.Model):  # 校园卡模型3
    no = models.CharField(max_length=8)  # 卡号
    stu = models.OneToOneField(stus3, on_delete=models.CASCADE, null=True)  # 外键，关联学生模型3

    def __str__(self):
        return "no=%s;stu_xm=%s" % (self.no, self.stu.xm)
