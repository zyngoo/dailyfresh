# coding:utf-8

from django.shortcuts import render, redirect
from df_user.isLogin import login
from models import *
from django.http import JsonResponse


@login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    print(uid)
    print(carts)
    lenn = len(carts)
    context = {
        "page_name":1,
        "title":"购物车",
        "carts":carts,
        "len":lenn,
    }
    return render(request, "df_cart/cart.html",context)


@login
def add(request,gid,count):
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)

    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    print(carts)
    if len(carts)>0:
        cart = carts[0]
        cart.count = cart.count+count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()

    count_s = CartInfo.objects.filter(user_id=uid).count()
    request.session['count'] = count_s

    if request.is_ajax():
        return JsonResponse({"count":count_s})

    else:
        return redirect("/cart/")


@login
def edit(request, cart_id, count):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        count1 = cart.count = int(count)
        cart.save()
        data = {"ok":0}
    except Exception as e:
        data = {"ok":count1}
    return JsonResponse(data)


@login
def delete(request, cart_id):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data = {"ok":1}
    except Exception as e:
        data = {"ok":0}
    return  JsonResponse(data)

