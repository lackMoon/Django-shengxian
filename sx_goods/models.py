from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class TypeInfo(models.Model):
    TypeTitle=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    def __str__(self):
        return self.TypeTitle.encode('utf-8')
class GoodsInfo(models.Model):
    GoodsTitle=models.CharField(max_length=20)
    GoodsPic=models.ImageField(upload_to='goods_list')
    GoodsPrice=models.DecimalField(max_digits=5,decimal_places=2)
    GoodsUnit=models.CharField(max_length=20)   #商品单位重量
    GoodsClickRate=models.IntegerField()   #商品点击量
    GoodsIntroduce=models.CharField(max_length=200) #商品简介
    GoodsStorage=models.IntegerField()      #商品库存
    GoodsContent=HTMLField()        #商品内容
    GoodsType=models.ForeignKey(TypeInfo,on_delete=models.CASCADE)
    isDelete=models.BooleanField(default=False)
