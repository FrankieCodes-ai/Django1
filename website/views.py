from .forms import CreateUserForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import  authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from .forms import CreateUserForm, LoginForm, createRecordForm

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
            return redirect('dashboard')
        
    context = {'create_form':form}
    return render(request,'website/create-record.html', context=context)
def user_logout(request):

    auth.logout(request)
    return redirect("my-login")