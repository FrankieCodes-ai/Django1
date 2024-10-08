from .forms import CreateUserForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import  authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from .forms import CreateUserForm, LoginForm, createRecordForm, UpdateRecordForm
from django.contrib import messages

# Dashboard
@login_required(login_url='my-login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records' : my_records}

    return render(request, 'website/dashboard.html', context=context)


def home(request):
    return render(request, 'website/index.html')

def register(request):
    form = CreateUserForm()
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return redirect('')
    context = {'form': form}

    return render(request,'website/register.html', context=context)

def my_login(request):
    form = LoginForm(request, data=request.POST)

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

        if user is not  None:
            auth.login(request, user)
            return redirect ('dashboard')

    context = {'login_form':form}
    return render(request,'website/my-login.html', context=context)

def create_record(request):
    form = createRecordForm()

    if request.method == "POST":
        form = createRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was created!")
            return redirect('dashboard')
        
    context = {'create_form':form}
    return render(request,'website/create-record.html', context=context)
def user_logout(request):

    auth.logout(request)
    messages.success(request, "Your have been logged out!")
    return redirect("my-login")

@login_required(login_url='my-login')
def update_record(request, pk):
    
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(request.POST, instance=record)
    
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            messages.success(request, "Your Record was updated!")
            return redirect("dashboard")

    context = {'update_form': form}
    return render(request, 'website/update-record.html', context=context)

@login_required(login_url='my-login')
def singular_record(request, pk):
    
    one_record = Record.objects.get(id=pk)
    context = {'record':one_record}
    return render(request, 'website/view-record.html', context=context)

@login_required(login_url='my-login')
def games(request):
    return render(request, 'website/games.html')

