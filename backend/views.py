from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError

from backend.models import admindb,itemdb,productdb,admin


def index(request):
    return render(request, "index.html")

def Addadmin(request):
    return render(request, "Addadmin.html")

def Saveadmin(request):
    if request.method == 'POST':
        na = request.POST.get('Name')
        em = request.POST.get('Email')
        mo = request.POST.get('Mobile')
        us = request.POST.get('Username')
        pa = request.POST.get('Password')
        img = request.FILES['image']
        obj = admindb(Name=na,Email=em,Mobile=mo,Username=us,Password=pa,image=img)
        obj.save()
        messages.success(request, "success")
        return redirect(Addadmin)

def Displayadmin(request):
    data = admindb.objects.all()
    return render(request, "Displayadmin.html", {'data': data})

def editadmin(req,dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(req, "Editadmin.html", {'data':data})

def updatedata(request,dataid):
    if request.method == 'POST':
        na = request.POST.get('Name')
        em = request.POST.get('Email')
        mo = request.POST.get('Mobile')
        us = request.POST.get('Username')
        pa = request.POST.get('Password')
        try:
            img=request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).image
        admindb.objects.filter(id=dataid).update(Name=na,Email=em,Mobile=mo,Username=us,Password=pa,image=file)
        messages.success(request, "success")
        return redirect(Displayadmin)

def deletedata(request, dataid):
    data= admindb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "success")
    return redirect(Displayadmin)

def categorypage(request):
    return render(request, "Category.html")

def saveitem(request):
    if request.method == 'POST':
        na = request.POST.get("Name")
        de = request.POST.get("Description")
        img = request.FILES['Image']
        obj = itemdb(Name=na,Description=de,Image=img)
        obj.save()
        messages.success(request, "success")
        return redirect(categorypage)

def displayitem(request):
    data=itemdb.objects.all()
    return render(request, "Displaycategory.html",{'data':data})

def edititem(req, dataid):
    data=itemdb.objects.get(id=dataid)
    print(data)
    return render(req, "Editcategory.html", {'data':data})

def updateitem(request,dataid):
    if request.method == 'POST':
        na = request.POST.get('Name')
        de = request.POST.get('Description')
        try:
            img = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = itemdb.objects.get(id=dataid).Image
        itemdb.objects.filter(id=dataid).update(Name=na, Description=de, Image=file)
        messages.success(request, "success")
        return redirect(displayitem)


def deleteitem(request, dataid):
    data = itemdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "success")
    return redirect(displayitem)

def productpage(request):
    data=itemdb.objects.all()
    return render(request, "product.html",{'data':data})


def saveproduct(request):
    if request.method == 'POST':
        ca = request.POST.get('category')
        pn = request.POST.get('productname')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        de = request.POST.get('description')
        img = request.FILES['image']
        obj = productdb(category=ca, productname=pn, price=pr, quantity=qu, description=de, image=img)
        obj.save()
        messages.success(request, "success")
        return redirect(productpage)


def displayproduct(request):
    data = productdb.objects.all()
    return render(request, "Displayproduct.html", {'data': data})


def editproduct(req, dataid):
    data = productdb.objects.get(id=dataid)
    da = itemdb.objects.all()
    print(data)
    return render(req, "Editproduct.html", {'data': data,'da':da})


def updateproduct(request, dataid):
    if request.method == 'POST':
        ca = request.POST.get('category')
        pn = request.POST.get('productname')
        pr = request.POST.get('price')
        qu = request.POST.get('quantity')
        de = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).image
        productdb.objects.filter(id=dataid).update(category=ca, productname=pn, price=pr, quantity=qu, description=de, image=file)
        messages.success(request, "success")
        return redirect(displayproduct)


def deleteproduct(request, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "success")
    return redirect(displayproduct)


def loginpage(rqst):
    return render(rqst, "login.html")


def adminlogin(rqst):
        if rqst.method == "POST":
            username_r = rqst.POST.get('username')
            password_r = rqst.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(rqst, user)
                rqst.session['username']=username_r
                rqst.session['password']=password_r
                messages.success(rqst, "login successfully")
                return redirect(index)
            else:
                messages.error(rqst, "invalid user")
                return redirect(loginpage)
        else:
            messages.error(rqst, "invalid user")
            return redirect(loginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "logout successfully")
    return redirect(loginpage)

def admintable(request):
    data = admin.objects.all()
    return render(request, "admintable.html", {'data': data})


def deleteadmin(request, dataid):
    data = admin.objects.filter(id=dataid)
    data.delete()
    messages.success(request, "success")
    return redirect(admintable)







