from django.shortcuts import render, redirect
from backend.models import itemdb, productdb, admin
from frontend.models import registerdb
from django.contrib import messages


# Create your views here.


def homepage(request):
    data = itemdb.objects.all()
    return render(request, "homepage.html", {'data': data})


def about(req):
    data = itemdb.objects.all()
    return render(req, "about.html", {'data': data})


def contact(req):
    data = itemdb.objects.all()
    return render(req, "contact.html", {'data': data})


def discategory(request, itemCatg):
    data = itemdb.objects.all()
    print("===itemcatg===", itemCatg)
    catg = itemCatg.upper()

    products = productdb.objects.filter(category=itemCatg)
    context = {
        'products': products,
        'catg': catg,
        'data': data
    }
    return render(request, "discategory.html", context)


def details(req, dataid):
    data = productdb.objects.get(id=dataid)
    messages.success(req, "Added to cart")
    return render(req, "details.html", {'dat': data})


def form(req):
    data = itemdb.objects.all()
    return render(req, "form.html", {'data': data})


def formreg(request):
    if request.method == 'POST':
        na = request.POST.get('username')
        em = request.POST.get('email')
        pa = request.POST.get('password')
        cp = request.POST.get('confirmpassword')
        obj = registerdb(username=na, email=em, password=pa, confirmpassword=cp)
        obj.save()
        messages.success(request, "registered successfully")
        return redirect(form)
    else:
        messages.error(request, "invalid")
        return render(request, "form.html")





def customerlogin(request):
    if request.method == 'POST':
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if registerdb.objects.filter(username=username_r, password=password_r).exists():
            request.session['username'] = username_r
            request.session['password'] = password_r
            messages.success(request, "login successfully")
            return redirect(homepage)
        else:
            messages.error(request, "invalid user")
            return render(request, "form.html")


def customerlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "logout successfully")
    return redirect(form)


def condet(request):
    if request.method == 'POST':
        na = request.POST.get('username')
        em = request.POST.get('email')
        su = request.POST.get('subject')
        me = request.POST.get('message')
        obj = admin(username=na, email=em, subject=su, message=me)
        obj.save()
        messages.success(request, "message sent successfully")
        return redirect(contact)


