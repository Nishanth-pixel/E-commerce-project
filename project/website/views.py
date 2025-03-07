from django.shortcuts import render,redirect
from .models import database,admin,addtocart,men,women

# Create your views here.

def main(request):
    return render(request,"main.html")

def demo(request):    
    return render(request,"home.html")

def home(request,id):
    a=admin.objects.all() 
    user=database.objects.get(id=id)
    d={"all":a,"user":user}
    return render(request,"index.html",d)

def mens(request,id):
    a=men.objects.all() 
    user=database.objects.get(id=id)
    d={"all":a,"user":user}
    return render(request,'men.html',d)
def womens(request,id):
    a=women.objects.all() 
    user=database.objects.get(id=id)
    d={"all":a,"user":user}
    return render(request,"women.html",d)
def about(request,id):
    a=admin.objects.all() 
    user=database.objects.get(id=id)
    d={"user":user}
    return render(request,'about.html',d)
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')


def loginpage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        database.objects.create(username=username,password=password,phonenumber=phone,email=email)
        return render(request,"login.html")
      

def all(request):
        a=database.objects.all()
        s={"all":a}
        return render(request,"database.html",s)

    
def userlogin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if database.objects.filter(username=username,password=password).exists():
            user=database.objects.filter(username=username,password=password).first()     
            a=admin.objects.all() 
            print(user.id)
            d={"all":a,"user":user}
            return render(request,"index.html",d)
                      
        else:
            return render(request,"login.html")

def adminview(request):
    return render(request,"admin.html")

def details(request):
     if request.method=="POST":
        productname=request.POST.get("productname")
        offerprice=request.POST.get("offerprice")
        image=request.FILES.get('image')
        productprice=request.POST.get("productprice")
        percentage=request.POST.get("percentage")
        admin.objects.create(productname=productname,offerprice=offerprice,productprice=productprice,image=image,percentage=percentage)
        a=admin.objects.all() 
        d={"all":a}
        return redirect(home)
     
     

def addproduct_men(request):
     if request.method=="POST":
        productname=request.POST.get("productname")
        offerprice=request.POST.get("offerprice")
        image=request.FILES.get('image')
        productprice=request.POST.get("productprice")
        percentage=request.POST.get("percentage")
        men.objects.create(productname=productname,offerprice=offerprice,productprice=productprice,image=image,percentage=percentage)
        a=men.objects.all() 
        d={"all":a}
        return redirect(mens) 

def addproduct_women(request):
     if request.method=="POST":
        productname=request.POST.get("productname")
        offerprice=request.POST.get("offerprice")
        image=request.FILES.get('image')
        productprice=request.POST.get("productprice")
        percentage=request.POST.get("percentage")
        women.objects.create(productname=productname,offerprice=offerprice,productprice=productprice,image=image,percentage=percentage)
        a=women.objects.all() 
        d={"all":a}
        return redirect(womens)


     
def addcard(request,id,pid):
    p=admin.objects.get(id=pid)
    addtocart.objects.create(cid=id,productname=p.productname,offerprice=p.offerprice,productprice=p.productprice,image=p.image,percentage=p.percentage)
    user=database.objects.get(id=id)
    a=addtocart.objects.filter(cid=id).values
    d={"user":user,"all":a}
    return render(request,"addtocart.html",d)

def addcard(request,id,pid):
    p=men.objects.get(id=pid)
    addtocart.objects.create(cid=id,productname=p.productname,offerprice=p.offerprice,productprice=p.productprice,image=p.image,percentage=p.percentage)
    user=database.objects.get(id=id)
    a=addtocart.objects.filter(cid=id).values
    d={"user":user,"all":a}
    return render(request,"addtocart.html",d)

def addcard(request,id,pid):
    p=women.objects.get(id=pid)
    addtocart.objects.create(cid=id,productname=p.productname,offerprice=p.offerprice,productprice=p.productprice,image=p.image,percentage=p.percentage)
    user=database.objects.get(id=id)
    a=addtocart.objects.filter(cid=id).values
    d={"user":user,"all":a}
    return render(request,"addtocart.html",d)



def mycard(request,id):
    user=database.objects.get(id=id)
    a=addtocart.objects.filter(cid=id).values
    d={"all":a,"user":user}
    return render(request,"addtocart.html",d)



def delete(request,id,cid):
    user=database.objects.get(id=cid)
    addtocart.objects.get(id=id).delete()
    a=addtocart.objects.filter(cid=cid).values
    d={"all":a,"user":user}
    return render(request,"addtocart.html",d)

def home(request,id):
    user=database.objects.get(id=id)
    a=admin.objects.all() 
    print(user.id)
    d={"all":a,"user":user}
    return render(request,"index.html",d)





     



    



   