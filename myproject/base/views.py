

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flight, Booking



def home(request):
    flights = Flight.objects.all()
    return render(request, "home.html", {"flights": flights})


def booking(request, flight_id):
    
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == "POST":
        Booking.objects.create(
            flight=flight,
            passenger_name=request.POST['passenger_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            seat_number=request.POST['seat_number'],
            seat_class=request.POST['seat_class']
        )
        return redirect("history")

    return render(request, "booking.html", {"flight": flight})


def history(request):
    bookings = Booking.objects.all().order_by('-created')
    return render(request, "history.html", {"bookings": bookings})


def cancel_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.status = "Cancelled"
    booking.save()
    return redirect("history")



# Authentication Views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect("register")

        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created! You may now log in.")
        return redirect("login")

    return render(request, "register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        messages.error(request, "Invalid username or password.")
        return redirect("login")
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("home")
