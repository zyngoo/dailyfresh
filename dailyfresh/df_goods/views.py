# coding:utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator


def index(request):
    count = request.session.get("count")
    fruit = GoodInfo.objects.filter(gtype__id=1).order_by("id")[:4]
    fruit2 = GoodInfo.objects.filter(gtype__id=1).order_by("-gclick")[:4]
    fish = GoodInfo.objects.filter(gtype__id=2).order_by("id")[:4]
    fish2 = GoodInfo.objects.filter(gtype__id=2).order_by("-gclick")[:4]
    meat = GoodInfo.objects.filter(gtype__id=3).order_by("-id")[:4]
    meat2 = GoodInfo.objects.filter(gtype__id=3).order_by("-gclick")[:4]
    egg = GoodInfo.objects.filter(gtype__id=4).order_by("-id")[:4]
    egg2 = GoodInfo.objects.filter(gtype__id=4).order_by("-gclick")[:4]
    vagetables = GoodInfo.objects.filter(gtype__id=5).order_by("-id")[:4]
    vagetables2 = GoodInfo.objects.filter(gtype__id=5).order_by("-gclick")[:4]
    frozen = GoodInfo.objects.filter(gtype__id=6).order_by("-id")[:4]
    frozen2 = GoodInfo.objects.filter(gtype__id=6).order_by("-gclick")[:4]


    context = {
        "guest_cart":1, "page_name":0,"count":count,
        "title":"首页", "fruit":fruit,"fruit2":fruit2,
        "fish":fish,"fish2":fish2,"meat":meat,
        "meat2":meat2,"egg":egg,"egg2":egg2,
        "vagetables":vagetables,"vagetables2":vagetables2,
        "frozen":frozen,"frozen2":frozen2
    }
    return render(request,"df_goods/index.html",context)


def list(request, typeid, pageid, sort):
    count = request.session.get("count")
    newgood = GoodInfo.objects.all().order_by("id")[:2]

    if sort == "1":
        sumGoodList = GoodInfo.objects.filter(gtype__id=typeid).order_by("id")
    elif sort=="2":
        sumGoodList = GoodInfo.objects.filter(gtype__id=typeid).order_by("gprice")
    elif sort=="3":
        sumGoodList = GoodInfo.objects.filter(gtype__id=typeid).order_by("-gclick")

    paginator = Paginator(sumGoodList, 15)
    goodList = paginator.page(int(pageid))
    pindexlist = paginator.page_range

    goodtype = TypeInfo.objects.get(id=typeid)

    context = {
        "title":"商品详情","list":1, "guest_cart":1,
        "goodtype":goodtype,"newgood":newgood,"goodList":goodList,
        "typeid":typeid, "sort":sort, "count":count,
        "pindexlist":pindexlist, "pageid":int(pageid)
    }
    print(sort)
    return render(request, "df_goods/list.html", context)


def detail(request, id):
    goods = GoodInfo.objects.get(pk=int(id))
    goods.gclick += 1
    goods.save()

    goodtype = goods.gtype

    count = request.session.get("count")

    news = goods.gtype.goodinfo_set.order_by("id")[:2]

    context = {
        "title":goods.gtype.ttitle, "guest_cart":1,
        "g":goods,"newgood":news, "id":id,"count":count,
        "isDetail":True, "list":1, "goodtype":goodtype
    }


    response = render(request, "df_goods/detail.html",context)

    goods_ids = request.COOKIES.get("goods_ids", "")
    goods_id = "%d" % goods.id
    if goods_ids != "":
        goods_ids1 = goods_ids.split(",")
        if goods_ids1.count(goods_id)>=1:
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0,goods_id)
        if len(goods_ids1)>5:
            del goods_ids1[5]
        goods_ids = ",".join(goods_ids1)
    else:
        goods_ids = goods_id
    response.set_cookie("goods_ids",goods_ids)

    return response