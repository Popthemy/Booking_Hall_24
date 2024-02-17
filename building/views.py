from django.shortcuts import render, redirect
from django.contrib import messages
from booking.models import MainSchedule
from .models import Hall
from .forms import HallForm
# Create your views here.

def halls(request):
    halls = Hall.objects.all()
    context = {'halls': halls}

    return render(request, 'halls.html',context)

def single_hall(request, pk):
    hall = Hall.objects.get(pk=pk) # get single hall
    hall_schedules = MainSchedule.objects.filter(pre_schedule__hall=hall) # get all schedule where these hall been booked
    
    context = {'hall': hall, 'hall_schedules': hall_schedules}

    return render(request, 'single-hall.html',context)



def createHall(request):
    forms = HallForm()

    if request.POST:
        forms = HallForm(request.POST,request.FILES)
        if forms.is_valid():
            hall_form = forms.save(commit=False)
            hall_form.name = hall_form.name.upper()
            print(hall_form.name)

            
            forms.save()
            message = 'You have succefully added a new hall.'
            messages.success(request,message)
            return redirect('/')
    context = { 'forms': forms}
    return render(request, 'hall-form.html', context)
        
    

def deleteHall(request,pk):
 
    hall = Hall.objects.get(pk=pk)

    if request.POST:

        hall.delete()
        message = 'You have succefully delete a hall.'
        messages.success(request,message)
        return redirect('/')
    
    context = { 'hall': hall}
    return render(request, 'delete-hall.html', context)

