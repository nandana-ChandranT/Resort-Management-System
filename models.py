from django.db import models



from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    floor = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.room_number

# class Reservation(models.Model):
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     guest_name = models.CharField(max_length=100)
#     check_in_date = models.DateField()
#     check_out_date = models.DateField()
#
#     def __str__(self):
#         return f"{self.guest_name}'s Reservation"
#
# class Guest(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=15)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
