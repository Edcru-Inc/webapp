from django.shortcuts import render, redirect, get_object_or_404
from .models import content
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

def index(request):
    contents = content.objects.all()
    return render(request, 'main/index.html', {'contents':contents})
# AUTH
@csrf_exempt
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'main/signup.html',{'message':'Enter the credentials'})

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('loginuser')
                return render(request, 'main/signup.html',{'message':'Successfully logged in!'})
            except IntegrityError:
                return render(request, 'main/signup.html',{'message':'Username already taken'})
        else:
            return render(request, 'main/signup.html',{'message':'Password do not match!'})

@csrf_exempt
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'main/login.html',{'message':'Enter the credentials'})

    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/login.html', {'message':'Username and password did not match'})
        else:
            login(request, user)
            return render(request, 'main/index.html')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'main/index.html')

