from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import User1
# Create your views here.

def login_request(request):
     if request.method == "POST":
          email = request.POST["email"]
          password = request.POST["password"]

          user = authenticate(request, email = email, password = password)

          if user is not None:
               login(request, user)
               return redirect("index")
          else:
               return render(request, "account/login.html", {
                    "error":"invalid email or password"
               })
     return render(request, "account/login.html")

def register_request(request):
    if request.method == "POST":
         name = request.POST["name"]
         lastname = request.POST["lastname"]
         email = request.POST["email"]
         password = request.POST["password"]
         country = request.POST["country"]
         city = request.POST["city"]


         user = User1(name=name, lastname=lastname, email=email, password=password, country=country, city=city)
         user.save()
         return redirect("login")
    return render(request, "account/register.html")
