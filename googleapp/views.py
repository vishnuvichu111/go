from django.http import HttpResponseRedirect, request, HttpResponse
from django.shortcuts import render, redirect
from .forms import logform
from .models import log

# Create your views here.
def login(request):
    sample1=logform()
    if request.method=='POST':
        sample1=logform(request.POST)
        if sample1.is_valid():
            sample1.save()
            #msg="login succefully"
            return HttpResponse("Sign Up Is Succesfull Please LogIn")
        else:
            sample1=logform()
    return render(request,'login.html',{'forms':sample1})
def signup(request):
    return render(request,'signup.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        if log.objects.filter(username=username, password=password).exists():
            return render(request, 'loged.html')
        else:
            msg = "invalied user name or password"
            return render(request, 'signup.html', {'msg': msg})
    else:
        return redirect('login')
def logout(request):
    logout(request)
    return redirect('login')
