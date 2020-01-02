# Generated by Django 2.1.1 on 2020-01-01 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='电影名称')),
                ('movie_cate', models.CharField(blank=True, max_length=30, null=True, verbose_name='电影分类')),
                ('release_date', models.DateField(verbose_name='上映日期')),
                ('viewed', models.BooleanField(default=False, verbose_name='观看状态')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': '电影',
                'verbose_name_plural': '电影',
            },
        ),
    ]