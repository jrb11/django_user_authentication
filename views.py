
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    #check user is anonumous or not
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # For coding verification
        print(username , password)
        
        # check user authentication
        user = authenticate(username=username, password=password)
        print("Authentication Done...")
        

        if user is not None:
            # Backend Authenticated credentials
            login(request, user)
            print("inside if ...")
            return redirect("/")
        else:
            #No backend authenticated credentials
            print("inside else...")
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')
    
