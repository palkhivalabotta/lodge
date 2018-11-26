from django.db import models
import datetime


#USER

class register(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    email_id = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
class check_availability(models.Model):
    room_number = models.IntegerField(primary_key=True)
    check_in = models.DateField()
    check_out = models.DateField()
class booking_room(models.Model):
    room_number = models.ForeignKey(check_availability,on_delete=models.CASCADE)
    credit_card = models.IntegerField()
    room_type = models.CharField(primary_key=True,max_length=10)
    check_in = models.DateField()
    check_out = models.DateField()
class display(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    username=models.CharField(max_length=100)
    room_number = models.ForeignKey(booking_room, on_delete=models.CASCADE)
    #room_type = models.ForeignKey(booking_room,on_delete=models.CASCADE)
    total_cost = models.IntegerField()
class cancel(models.Model):
    username = models.CharField(max_length=100)
    room_number = models.ForeignKey(booking_room,on_delete=models.CASCADE)
    email_id = models.EmailField(max_length=100)


