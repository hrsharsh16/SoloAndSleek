from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse



from.models import User
# Create your views here.
def index(request):
    return render(request,"soloandsleek/home.html")

def login_view(request):
    if request.method == "POST":
        #retreive from post request
        email = request.POST["email"]
        password = request.POST["password"]
        
        #attempt login
        user = authenticate(request, username=email, password=password)

        #check if authntication success
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "soloandsleek/login.html", {
                "message" : "Invalid, try again."
            })

    else:
        return render(request,"soloandsleek/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

def register(request):
    if request.method == "POST":
        #retreive from post request
        email = request.POST["email"]
        password = request.POST["password"]

        #attempt to create a user
        try:
            user = User.objects.create_user(email, email, password)
            user.save
        except IntegrityError as e:
            print(e)
            return render(request, "soloandsleek/register.html", {
                "message" : "account already exists."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))

    else:
        return render(request,"soloandsleek/register.html")
    

#login logout, destinations, your itenary for a specific trip, create a trip, hotels, flights, activities