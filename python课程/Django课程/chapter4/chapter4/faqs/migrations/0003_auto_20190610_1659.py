# Generated by Django 2.1.7 on 2019-06-10 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0002_shet_stus'),
    ]

    operations = [
        migrations.CreateModel(
            name='shet2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mc', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='ssRelations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jdate', models.DateField()),
                ('st', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faqs.shet2')),
            ],
        ),
        migrations.CreateModel(
            name='stus2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xm', models.CharField(max_length=8)),
                ('shets', models.ManyToManyField(through='faqs.ssRelations', to='faqs.shet2')),
            ],
        ),
        migrations.AddField(
            model_name='ssrelations',
            name='stu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faqs.stus2'),
        ),
    ]
