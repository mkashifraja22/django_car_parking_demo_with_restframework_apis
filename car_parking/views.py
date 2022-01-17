from django.shortcuts import render, redirect
from .models import Slots


# Create your views here.

def index(request):
    slots = Slots.objects.all()
    context = {

        "slots": slots
    }
    return render(request, "index.html", context)


def park(request):
    if request.method == 'POST':
        slot_id = request.POST.get("slot", 0)
        car_number = request.POST.get("car_number")
        slot = Slots.objects.get(id=slot_id)
        slot.vehicle_no = car_number
        slot.save()
    return redirect("index")


def unpark(request, id):
    slot = Slots.objects.get(id=id)
    slot.vehicle_no = ""
    slot.save()
    return redirect("index")


def search(request):
    return redirect('index')
