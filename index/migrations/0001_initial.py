# Generated by Django 4.0.1 on 2022-01-12 02:20

from django.db import migrations, models
import index.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='书名')),
                ('public', models.CharField(max_length=50, verbose_name='出版社')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='定价')),
                ('retail_price', models.DecimalField(decimal_places=2, default=index.models.Book.default_price, max_digits=7, verbose_name='零售价')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=24, verbose_name='用户注册')),
                ('password', models.CharField(max_length=24, verbose_name='密码')),
            ],
        ),
    ]
