# -*-coding: utf-8 -*-
from django.contrib import admin
from news.models import new,cate
# Register your models here.

class adminNews(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("new_title", "new_id", "new_seenum", "new_time",'new_cate',)
    # 添加search bar，在指定的字段中search
    search_fields = ("new_title", "new_time",'new_cate',)
    # 页面右边会出现相应的过滤器选项
    list_filter = (  "new_time",'new_cate',)
    # 排序
    ordering = ("-new_time",)

admin.site.register(new, adminNews)

class adminCate(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("cate_id", "cate_name",)
    # 添加search bar，在指定的字段中search
    search_fields = ("cate_id", "cate_name",)
    # 页面右边会出现相应的过滤器选项
    list_filter = (  "cate_name",)

admin.site.register(cate, adminCate)
