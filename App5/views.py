from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from App5.models import RegisterModel
from App5.models import LoginModel, TwitterModel, HomeModel
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy

def register(request):
    return render(request, "register.html")

def register_up(request):
    name = request.POST.get("r1")
    username = request.POST.get("r2")
    mail = request.POST.get("r3")
    contact = request.POST.get("r4")
    password = request.POST.get("r5")
    if len(str(contact)) == 10:
        RegisterModel(Name=name,Username=username,Email=mail,Contact=contact,Password=password).save()
        LoginModel(Username=username,Password=password).save()
        messages.success(request,"Registered Successfully")
        return redirect("register")
    else:
        return redirect("register", {"error":"Invalid number"})

def login(request):
    return render(request, "login.html")

def login_up(request):
    username = request.POST.get("l1")
    password = request.POST.get("l2")
    try:
        LoginModel.objects.get(Username=username, Password=password)
        return render(request, "login1.html", {"name": username})
    except LoginModel.DoesNotExist:
        return render(request, "login.html", {"error": "Username and Password doesn't match"})

def login1(request):
    return render(request, "login1.html")

def twitter(request):
    return render(request, "twitter.html")

def twitter_up(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")
    try:
        TwitterModel.objects.get(Username=username, Password=password)
        return render(request, "login1.html", {"name": username})
    except TwitterModel.DoesNotExist:
        user = request.POST.get("t1")
        passw = request.POST.get("t2")
        TwitterModel(Username=user, Password=passw).save()
        return render(request, "login1.html")

def home(request):
    return render(request, "home.html")

def home_save(request):
    name = request.POST.get("a1")
    username = request.POST.get("a2")
    comment = request.POST.get("a3")
    upload = request.FILES["a4"]
    HomeModel(Name=name, UserName=username, Comments=comment, Uploads=upload).save()
    messages.success(request, "Thank you for uploading and for your response with smile")
    return redirect("home")

def view(request):
    username=request.GET.get("un")
    try:
        s_view=HomeModel.objects.get(UserName=username)
        return render(request, "view.html", {"name": username, "data": s_view})
    except HomeModel.DoesNotExist:
        return redirect("login1")

def update(request):
    username = request.GET.get("un")
    try:
        s_update = HomeModel.objects.get(UserName=username)
        return render(request, "update.html", {"name": username, "data": s_update})
    except HomeModel.DoesNotExist:
        return redirect("login1")

def update_save(request):
    name = request.POST.get("u1")
    username = request.POST.get("u2")
    comment = request.POST.get("u3")
    upload = request.FILES["u4"]
    try:
        HomeModel.objects.filter(UserName=username).update(Name=name, Comments = comment, Uploads=upload)
        return render(request, "login1.html", {"name": username})
    except HomeModel.DoesNotExist:
        return render(request, "login1.html", {"name": username})

def viewall(request):
    s_viewall = HomeModel.objects.all()
    return render(request, "viewall.html", {"data": s_viewall})

def delete(request):
    de = request.GET.get("no")
    HomeModel.objects.filter(UserName=de).delete()
    return render(request, "login1.html")






