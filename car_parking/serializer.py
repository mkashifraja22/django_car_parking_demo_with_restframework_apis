from .models import Slots
from rest_framework import  serializers


class SlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slots
        fields = "__all__"