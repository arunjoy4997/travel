from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('/credentials/register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('/credentials/register')

            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save();
                return redirect('/credentials/login')
        else:
            messages.info(request,'password not matching')
            return redirect('/credentials/register')

        return redirect('/')

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/credentials/login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')