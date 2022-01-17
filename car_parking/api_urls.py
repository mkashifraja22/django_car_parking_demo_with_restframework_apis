from django.urls import path
from .views_api import *

urlpatterns = [

    path("slots", list_slot, name="list_slot"),
    path("update/<int:pk>/", update, name="slot_update"),
    path("unpark/<int:pk>/", unpark, name="slot_unpark")
]
