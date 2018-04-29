# coding:utf-8
from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.ttitle.encode("utf-8")


class GoodInfo(models.Model):
    gtitle = models.CharField(max_length=20,default="维多利亚葡萄")
    gpic = models.ImageField(upload_to="df_goods")
    gprice = models.DecimalField(max_digits=5,decimal_places=2,default=38)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20,default="500g")
    gclick = models.IntegerField(default=0)
    gjianjie = models.CharField(max_length=200,default="这是一段葡萄的简介!")
    gkucun = models.IntegerField(default=100)
    gcontent = HTMLField(default="这是一段葡萄的介绍!")
    gtype = models.ForeignKey(TypeInfo)
    # gadv  = models.BooleanField(default=False)

    def __str__(self):
        return self.gtitle.encode("utf-8")
    

