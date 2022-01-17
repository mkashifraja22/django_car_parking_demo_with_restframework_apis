from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Slots
from .serializer import SlotsSerializer
from .utils import operation_success


@csrf_exempt
def list_slot(request):
    if request.method == "GET":

        slots = Slots.objects.all()
        serializer = SlotsSerializer(slots, many=True)
        data = operation_success(serializer.data)
        return JsonResponse(data)
    elif request.method == "POST":
        data = JSONParser().parse(request)

        serializer = SlotsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
@api_view(["PUT", "GET", "DELETE"])
def update(request, pk):
    try:
        slot = Slots.objects.get(pk=pk)
    except slot.DoesNotExist:
        HttpResponse(status=400)
    if request.method == "GET":
        serializer = SlotsSerializer(slot)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":

        data = request.data

        serializer = SlotsSerializer(slot, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        slot.delete()
        return HttpResponse(status=204)


@csrf_exempt
@api_view(["PUT"])
def unpark(request, pk):
    try:
        slot = Slots.objects.get(pk=pk)
    except slot.DoesNotExist:
        HttpResponse(status=400)
    if request.method == "PUT":
        slot.vehicle_no = ""
        slot.save()
        return Response(operation_success())

        # return JsonResponse(serializer.errors, status=400)
