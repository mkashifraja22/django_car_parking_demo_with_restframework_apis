from django.db import models

# Create your models here.

class Slots(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vehicle_no = models.TextField(max_length=50, null=True ,blank=True)


    # def __int__(self):
    #     return self.id
