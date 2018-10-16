#coding:utf-8
from django.conf.urls import url
from . import views
urlpatterns=[
    url('^register/$',views.register),
    url('^register_handle/$',views.register_handle),
    url('^user_exist/',views.user_exist),
    url('^login/$',views.login),
    url('^login_handle/$',views.login_handle),
    url('^login_varify/',views.login_varify),
    url('^userinfo/$',views.user_info),
]