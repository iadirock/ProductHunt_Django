from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
def signup(request):
    if request.method == 'POST':
        #USER NEED TO SIGN UP
        #checking the password
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'account/signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'account/signup.html',{'error':'password doesnot match'})
    else:
        #user wants to login
        return render (request, 'account/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render (request, 'account/login.html', {'error':'Username or password is incorrect'})    
    else:
        return render (request, 'account/login.html')

def logout(request):
    # TODO need to route to homepage
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
