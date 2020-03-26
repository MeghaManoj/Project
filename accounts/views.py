from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash


# Create your views here.

def registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")
        else:
            return render(request, "accounts/register.html", {"form":form})
    else:
        form = UserForm()
        return render(request, "accounts/register.html", {"form":form})

def login(request):
    # if request.user.is_authenticated:
    #    return redirect('/') 
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        check = authenticate(username=email,password=password)
        if check:
            login(request,check)
            return redirect("/")
        else:
            return render(request ,"accounts/login.html",{"login_error_msg":"username or password incorrect"})

    else:
        return render(request ,"accounts/login.html")