from django.shortcuts import render, redirect
from account.forms import regForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'account/index.html')

def register(request):
    if request.method =='POST':
        form = regForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = regForm()
        args = {'form': form}
        return render(request, 'account/registerForm.html', args)

def info(request):
    args = {'user': request.user}
    return render(request, 'account/info.html', args)