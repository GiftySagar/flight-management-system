from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('booking/<int:flight_id>/',booking, name='booking'),
    path('history/', history, name='history'),
    path('cancel/<int:id>/', cancel_booking, name='cancel'),

    
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]

