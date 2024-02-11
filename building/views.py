from django.shortcuts import render
from booking.models import Main_Schedule, Pre_Schedule
from .models import Hall

# Create your views here.

def halls(request):
    halls = Hall.objects.all()
    context = {'halls': halls}

    return render(request, 'halls.html',context)

def single_hall(request, pk):

    hall = Hall.objects.get(pk=pk) # get single hall
    hall_schedules = Main_Schedule.objects.filter(pre_schedule__hall=hall) # get all schedule where these hall been booked
    
    
    context = {'hall': hall, 'hall_schedules': hall_schedules}

    return render(request, 'single-hall.html',context)
