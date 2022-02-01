from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request,"cafe/about.html")
def home(request):
    return render(request,"cafe/home.html")
def reservation(request):
    return render(request,"cafe/reservation.html")
def team(request):
    return render(request,"cafe/team.html")
def special_dishes(request):
    return render(request,"cafe/special-dishes.html")
def menu(request):
    return render(request,"cafe/menu.html")