from django.contrib import admin
from django.urls import path
from website.views import demo,home,mens,womens,about,register,login,loginpage,userlogin,all,adminview,details,addcard,mycard,addproduct_men,addproduct_women,main,delete

urlpatterns = [
    path('demo',demo),
    path('',main),
    path('home/<id>',home),
    path('men/<id>',mens),
    path('women/<id>',womens),
    path('about/<id>',about),
    path('register',register),
    path('login',login),
    path('all',all),
    path('login_user',loginpage),
    path('userlogin',userlogin),
    path('admin',adminview),
    path('detail',details),
    path('productmen',addproduct_men),
    path('productwomen',addproduct_women),
    path('addcard/<id>/<pid>',addcard),
    path('cart/<id>',mycard),
    path('delete/<id>/<cid>',delete),
]

