# Generated by Django 2.2.2 on 2019-07-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter7', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=8, verbose_name='姓名'),
        ),
    ]
