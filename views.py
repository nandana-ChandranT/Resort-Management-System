

from django.shortcuts import render
from resort.models import Room
from django.http import HttpResponse

def home(request):
    return render(request,'base.html')
def index(request):
    return render(request,'index,html')

def room(request):
    rooms = Room.objects.all()
    return render(request, 'room.html', {'rooms':rooms})

# def reservation_list(request):
#     reservations = Reservation.objects.all()
#     return render(request, 'reservation_list.html', {'reservations': reservations})
#
# def room_detail(request, room_id):
#     room = Room.objects.get(pk=room_id)
#     return render(request, 'room_detail.html', {'room': room})
