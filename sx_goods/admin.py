from django.contrib import admin
from .models import *
# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ["id","TypeTitle"]
class GoodInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "GoodsTitle","GoodsPic","GoodsPrice","GoodsUnit","GoodsStorage", "GoodsIntroduce","GoodsContent","GoodsContent","GoodsType"]
    list_per_page = 15
admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodInfoAdmin)