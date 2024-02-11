from django.shortcuts import render
from .models import Main_Schedule,Pre_Schedule
# Create your views here.


def preSchedule(request,pk):

    context = {}
    return render(request, 'booking/pre-schedule.html',context)



def mainSchedule(request,pk):

    context = {}
    return render(request, 'booking/main-schedule.html',context)
