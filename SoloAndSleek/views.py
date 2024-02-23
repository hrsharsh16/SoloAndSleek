from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"soloandsleek/home.html")

#login logout, destinations, your itenary for a specific trip, create a trip, hotels, flights, activities