from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm

#create a record
@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()
    if request.method =="POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")
        
    context = {'create_form': form}
    return render(request, 'website/create-record.html',context=context)