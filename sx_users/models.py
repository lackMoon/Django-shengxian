from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_name=models.CharField(max_length=30)
    user_password=models.CharField(max_length=40)
    user_email=models.EmailField(max_length=20)
    user_emailcode=models.CharField(max_length=6,null=True)
    receive_user=models.CharField(max_length=20,null=True)
    user_phone=models.CharField(max_length=11,null=True)
class UserAddress(models.Model):
    user_address=models.CharField(max_length=100,null=True)
    users=models.ForeignKey('UserInfo',on_delete=models.CASCADE)