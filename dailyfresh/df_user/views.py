# coding:utf-8
from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.shortcuts import render,redirect, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from models import *
from hashlib import sha1
from . import isLogin
from df_goods.models import GoodInfo
from df_order.models import *
from df_cart.models import *

def register(request):
    return  render(request, "df_user/register.html",{"title":"天天生鲜-注册"})


def register_handle(request):
    post = request.POST
    uname = post.get("user_name")
    upwd = post.get("pwd")
    cpwd = post.get("cpwd")
    email = post.get("email")

    if upwd != cpwd:
        return redirect("/user/register/")
    #密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()


    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = email

    user.save()

    # 注册成功,转到登入页面
    return redirect("/user/login/")

  # register_exist
def register_exist(request):
    print("-----------")
    uname = request.GET.get("uname")
    print(uname)
    count = UserInfo.objects.filter(uname=uname).count() # count 要么返回0,要么返回1
    return JsonResponse({"count":count})



def login(request):
    # print("=========")
    uname = request.COOKIES.get("uname","")
    # print(uname)
    context = {"title":"天天生鲜-登录", "error_name":0, "error_pwd":0, "uname":uname}
    return render(request, "df_user/login.html",context)



def login_handle(request):
    post = request.POST
    uname = post.get("username")
    upwd = post.get("pwd")
    jizhu = post.get('jizhu', 0)

    # # 密码加密
    # s1 = sha1()
    # s1.update(upwd)
    # upwd3 = s1.hexdigest()
    #
    # obj = UserInfo.objects.get(uname = uname) #[]  使用get()容易出现异常
    #
    # if upwd3 == obj.upwd:
    #     request.session['uname'] = request.POST['username']
    #     return redirect("/user/user_center_info/")

    users = UserInfo.objects.filter(uname=uname)

    if len(users)==1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest()==users[0].upwd:
            url = request.COOKIES.get("url","/")
            red = HttpResponseRedirect(url)

            if jizhu != 0:
                red.set_cookie("uname",uname)
            else:
                red.set_cookie("uname","",max_age=-1)
            request.session["user_id"]= users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {"title": "天天生鲜-登录", "error_name": 0, "error_pwd": 1, "uname": uname,"upwd":upwd}
            return render(request, "df_user/login.html",context)
    else:
        context = {"title": "天天生鲜-登录", "error_name": 1, "error_pwd": 0, "uname": uname, "upwd": upwd}
        return render(request, "df_user/login.html", context)





@isLogin.login
def user_center_info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    user_address = UserInfo.objects.get(id=request.session['user_id']).uaddress

    goods_ids = request.COOKIES.get("goods_ids","")
    goods_ids1 = goods_ids.split(",")
    goods_list = []
    if len(goods_ids):
        for goods_id in goods_ids1:
            goods_list.append(GoodInfo.objects.get(id=int(goods_id)))

    context = {
        "title":"用户中心",
        "user_email":user_email,
        "user_name":request.session['user_name'],
        "user_address":user_address,
        "page_name":1,
        "info":1,
        # "site":1,
        # "order":1,
        "goods_list":goods_list
    }

    return render(request, "df_user/user_center_info.html",context)


@isLogin.login
def order(request):
    context = {"title":"用户中心"}
    return render(request, "df_user/user_center_order.html", context)


@isLogin.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method=='POST':
        post=request.POST
        user.ushou = post.get("ushou")
        user.uaddress = post.get("uaddress")
        user.uyoubian = post.get("uyoubian")
        user.uphone = post.get("uphone")
        user.save()
    context = {"title":"用户中心", "user":user}

    return render(request, "df_user/user_center_site.html",context)


def logout(request):
    request.session.flush()
    return redirect("/")


@isLogin.login
def user_center_order(request, pageid):
    uid = request.session.get("user_id")
    orderinfos = OrderInfo.objects.filter(user_id=uid).order_by("zhifu", "-oid")

    paginator = Paginator(orderinfos, 2)
    orderlist = paginator.page(int(pageid))

    plist = paginator.page_range

    qian1 = 0
    huo = 0
    huo2 = 0
    qian2 = 2

    dd = int(pageid)

    lenn = len(plist)
    if dd>1:
        qian1 = dd-1
    if dd>=3:
        qian2 = dd-2
    if dd<lenn:
        huo = dd+1
    if dd+2<=lenn:
        huo2 = dd+2


    context = {
        "page_name":1, "title":"全部订单", "pageid":int(pageid),
        "order":1, "orderlist":orderlist, "plist":plist,
        "pre":qian1, "next":huo, "pree":qian2, "lenn":lenn, "nextt":huo2
    }

    return render(request, "df_user/user_center_order.html", context)







'''
http://127.0.0.1:8000/200/?type=10
request.path:表示当前路径  /200/
request.get_full_path():表示完整路径 /200/?type=10
'''