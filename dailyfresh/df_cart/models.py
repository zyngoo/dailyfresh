from django.db import models

class CartInfo(models.Model):
    user = models.ForeignKey("df_user.UserInfo")
    goods = models.ForeignKey("df_goods.GoodInfo")
    count = models.IntegerField(default=0)
