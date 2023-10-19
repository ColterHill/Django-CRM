from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

def home(request):
    records = Record.objects.all()

    #check to see if loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have succesfully signed in!")
            return redirect('home')
        else:
            messages.success(request, "Please type in a correct username and password.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})



def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')