# Generated by Django 4.0.1 on 2022-01-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_extenduserinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(choices=[('M', '男性'), ('F', '女性')], default='M', max_length=10),
        ),
    ]
