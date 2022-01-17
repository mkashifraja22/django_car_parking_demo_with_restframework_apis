from django.urls import path
from car_parking import views as carparking_views

urlpatterns = [

    path("", carparking_views.index, name="index"),
    path("unpark-car/<int:id> ", carparking_views.unpark, name="unpark"),
    path("park-car", carparking_views.park, name="park")
]
