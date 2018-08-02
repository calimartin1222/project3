from django.shortcuts import render, redirect
from account.forms import regForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

global user_name

# Create your views here.
@login_required
def index(request):
    user_name = request.user
    args = {'user': request.user}
    return render(request, 'account/index.html', args)

def get_user():
    return user_name

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