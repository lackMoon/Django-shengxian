#coding:utf-8
from django.shortcuts import render,redirect
from hashlib import sha1
from .models import *
from django.http import JsonResponse,HttpResponseRedirect
from . import user_decorator
# Create your views here.
#注册
def register(request):
    return render(request,'sx_users/register.html',{'title':'天天生鲜-注册'})
def register_handle(request):
    post=request.POST
    uname=post.get("user_name")
    upwd=post.get("pwd")
    upwd_again=post.get("cpwd")
    uemail=post.get("email")
    if upwd!=upwd_again:
        return redirect("/user/register/")
    s1=sha1()
    s1.update(upwd.encode("utf8"))
    hex_upwd=s1.hexdigest()
    user=UserInfo()
    user.user_name=uname
    user.user_password=hex_upwd
    user.user_email=uemail
    user.save()
    return redirect('/user/login/')
def user_exist(request):
    uname=request.GET["uname"]
    return JsonResponse({'exist':UserInfo.objects.filter(user_name=uname).exists()})
#登陆
def login(request):
    uname=request.COOKIES.get("uname","")
    return render(request,'sx_users/login.html',{'title':'天天生鲜-登陆'})
def login_handle(request):
    post=request.POST
    uname=post.get("username")
    upwd=post.get("pwd")
    remember=post.get("remember")
    login_user=UserInfo.objects.filter(user_name=uname)[0]
    if upwd!=login_user.user_password:
        return redirect('/user/login/')
    url=request.COOKIES.get("url","/")
    red=HttpResponseRedirect(url)
    if remember==True:
        red.set_cookie('uname',uname)
    else:
        red.set_cookie('uname','',max_age=-1)
    request.session["user_id"]=login_user.id
    request.session['user_name']=uname
    request.session['user_email']=login_user.user_email
    return red
def login_varify(request):
    uname=request.GET["uname"]
    upwd=request.GET["upwd"]
    try:
        right_pwd=UserInfo.objects.filter(user_name=uname)[0].user_password
        s1 = sha1()
        s1.update(upwd.encode("utf8"))
        hex_upwd = s1.hexdigest()
        if hex_upwd==right_pwd:
            return JsonResponse({'varify':True})
        else:
            return JsonResponse({'varify':False})
    except Exception:
        return JsonResponse({'varify': False})
#用户中心
@user_decorator.login
def user_info(request):
    user_name=request.session["user_name"]
    user_email=request.session["user_email"]
    return render(request,"sx_users/user_center_info.html",{'title':'天天生鲜-用户中心','user_name':user_name,'user_email':user_email})
