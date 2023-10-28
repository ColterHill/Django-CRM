from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Record, Product, Opportunities
from .forms import SignUpForm, AddRecordForm, AddOppForm

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

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record has been deleted")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to perform this action")
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save(commit=False)
                add_record.primary_rep = User.objects.get(pk=request.user.id)
                add_record = form.save()
                messages.success(request, "Record has been added!")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You need to be signed in to add a record")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "You've successfully updated the record!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You need to be signed in to update a record")
        return redirect('home')
    
def accounts(request):
    records = Record.objects.all()
    
    if request.user.is_authenticated:
        return render(request, 'accounts.html', {'records':records})
    else:
        messages.success(request, "You must be logged in to view Accounts.")
        
def opportunities(request):
    opportunities = Opportunities.objects.all()
    
    if request.user.is_authenticated:
        return render(request, 'opportunities.html', {'opportunities':opportunities})
    else:
        messages.success(request, "You must be logged in to view Accounts.")
        
def opp_record(request, pk):
    if request.user.is_authenticated:
        # look up records
        opp_record = Opportunities.objects.get(id=pk)
        return render(request, 'opp_record.html', {'opp_record':opp_record})
    else:
        messages.success(request, "You must be logged in to view that page")
        return redirect('home')
        
        
def add_opp(request):
    form = AddOppForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_opp = form.save(commit=False)
                add_opp.opp_owner = User.objects.get(pk=request.user.id)
                add_opp = form.save()
                messages.success(request, "Opportunity has been added!")
                return redirect('opportunities')
        return render(request, 'add_opp.html', {'form':form})
    else:
        messages.success(request, "You need to be signed in to add a record")
        return redirect('home')
    
    
def products(request):
    products = Product.objects.all()
    
    if request.user.is_authenticated:
        return render(request, 'products.html', {'products':products})
    else:
        messages.success(request, "You must be logged in to view products.")