# Generated by Django 2.2.2 on 2019-07-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kh', models.CharField(max_length=8)),
                ('xm', models.CharField(max_length=8)),
                ('yw', models.IntegerField()),
                ('sx', models.IntegerField()),
                ('yy', models.IntegerField()),
            ],
        ),
    ]
