from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("LOGGED")
            # Redirect to a success page.
            return redirect('search')
        else:
            # Return an 'invalid login' error message.
            return redirect('login2')
    else:
        return render(request, "authenticate/login.html", {})

def logout_user(request):
    logout(request)
    return redirect('search')
