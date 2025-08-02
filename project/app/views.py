from django.shortcuts import *
from django.http import HttpResponse
from app.forms import Register,userlogin,search
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Jobs
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate, login
from .forms import userlogin


def homepage(request):
    return render(request,"homepage.html")

def signup(request):
    if request.method == 'POST':
        fn = Register(request.POST)
        if fn.is_valid():
            uname = fn.cleaned_data['username']
            fname = fn.cleaned_data['firstname']
            lname = fn.cleaned_data['lastname']
            email = fn.cleaned_data['email']
            pwd = fn.cleaned_data['password']
            repwd = fn.cleaned_data['reenter']

            if pwd != repwd:
                return HttpResponse("Passwords do not match")
            # ✅ Create user properly with hashing
            user = User.objects.create_user(username=uname, password=pwd, email=email, first_name=fname, last_name=lname)
            user.save()
            return redirect('/user_login')
    else:
        fn = Register()
    return render(request, 'signup.html', {'form': fn})


def user_login(request):
    if request.method == 'POST':
        fn = userlogin(request.POST)
        if fn.is_valid():
            uname = fn.cleaned_data['username']
            pwd = fn.cleaned_data['password']
            user = authenticate(username=uname, password=pwd)
            print(uname,pwd,user)
            if user is not None:
                login(request, user)
                return redirect('/profile')
            else:
                return HttpResponse("Invalid username or password")
        else:
            return render(request, "login.html", {'form': fn, 'errors': fn.errors})
    else:
        fn = userlogin()
    return render(request, "login.html", {'form': fn})

def profile(request):
    content={}
    content['data']=Jobs.objects.all()
    return render(request,"profile.html",content)

def search_job(request):
    if request.method=='POST':
        fn=search(request.POST)
        if fn.is_valid():
            value=fn.cleaned_data['job_title']
            data=Jobs.objects.filter(jobname=value)
            return render(request,'profile.html',{'data':data})
    else:
        fn=search()
    return render(request,'search.html',{"form":fn})

def user_details(request):
    return render(request,"details.html")

from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.models import User
# from django.http import HttpResponse
def edit(request, username):
    if request.method == "POST":
        uname=request.POST['uname']
        fn=request.POST['fname']
        ln=request.POST['lname']
        em=request.POST['email']
        user=User.objects.filter(username=username)
        user.update(username=uname,first_name=fn,last_name=ln,email=em)
        return redirect("/user_details")
    else:
        user = get_object_or_404(User, username=username)
        content = {'data': user}
        return render(request, 'edit_details.html', content)

