from .forms import CreateUserForm, LoginForm
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'website/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form': form}

    return render(request,'website/register.html', context=context)