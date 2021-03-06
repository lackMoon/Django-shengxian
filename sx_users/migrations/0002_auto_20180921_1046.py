# Generated by Django 2.0.4 on 2018-09-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sx_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='receive_user',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='user_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_emailcode',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_phone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
