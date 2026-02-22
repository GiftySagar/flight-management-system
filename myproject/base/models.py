from django.db import models

# Create your models here.


class Flight(models.Model):
    flight_no = models.CharField(max_length=20)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.flight_no} — {self.origin} to {self.destination}"


class Booking(models.Model):
    SEAT_CLASS_CHOICES = [
        ('Economy', 'Economy'),
        ('Business', 'Business'),
        ('First', 'First'),
    ]

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    seat_number = models.CharField(max_length=10)
    seat_class = models.CharField(max_length=10, choices=SEAT_CLASS_CHOICES)
    status = models.CharField(max_length=20, default="Booked")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger_name} - {self.flight.flight_no}"
