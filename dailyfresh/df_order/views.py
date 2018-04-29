# coding:utf-8

from django.shortcuts import render, redirect
from django.db import transaction
from datetime import datetime
from decimal import Decimal
from models import *
from df_user.isLogin import login
from df_cart.models import CartInfo
from df_goods.models import GoodInfo
from df_user.models import UserInfo
from django.http import JsonResponse


@login
def order(request):

    uid = request.session.get("user_id")
    user = UserInfo.objects.get(id=uid)

    orderid = request.GET.getlist("orderid")
    print(orderid)
    orderlist = []

    for id in orderid:
        orderlist.append(CartInfo.objects.get(id=int(id)))

    if user.uphone == "":
        uphone = ""
    else:
        uphone = user.uphone[:3] + "****" + user.uphone[-4:]



    context = {
        "title":"提交订单",
        "page_name":1,
        "orderlist":orderlist,
        "user":user,
        "ureceive_phone":uphone,
    }

    return render(request, "df_order/order.html",context)



@transaction.atomic()
@login
def order_handle(request):
    tran_id = transaction.savepoint()

    try:
        post = request.POST
        orderlist = post.getlist("id[]")
        print(orderlist)
        total = post.get("total")
        address = post.get("address")

        order = OrderInfo()
        now = datetime.now()
        uid = request.session.get("user_id")
        order.oid = "%s%d"%(now.strftime("%Y%m%d%H%M%S"), uid)
        order.user_id = uid
        order.odate = now
        order.ototal = Decimal(total)
        order.oaddress = address

        order.save()

        for orderid in orderlist:
            print(orderid)
            cartinfo = CartInfo.objects.get(id=orderid)
            good = GoodInfo.objects.get(pk=cartinfo.goods_id)

            if int(good.gkucun) >= int(cartinfo.count):
                good.gkucun -= int(cartinfo.count)
                good.save()

                goodinfo = GoodInfo.objects.get(cartinfo__id=orderid)

                print(goodinfo)

                detailinfo = OrderDetailInfo()
                detailinfo.goods_id = int(goodinfo.id)
                detailinfo.order_id = int(order.oid)
                detailinfo.price = Decimal(int(goodinfo.gprice))
                detailinfo.count = int(cartinfo.count)
                detailinfo.save()

                request.session['count'] = None
                cartinfo.delete()

            else:
                transaction.savepoint_rollback(tran_id)
                print("status:2")
                return JsonResponse({"status":2})

    except Exception as e:
        print("=================%s"%e)
        transaction.savepoint_rollback(tran_id)
        print("status:3")
        return JsonResponse({"status": 2})

    print("status:1")
    return JsonResponse({"status":1})


def pay(request, oid):
    order = OrderInfo.objects.get(oid=oid)
    order.zhifu = 1

    order.save()
    context = {"oid":oid}
    return render(request, "df_order/pay.html", context)

