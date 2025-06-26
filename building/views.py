from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from booking.models import MainSchedule


from .models import Hall
from .forms import HallForm

from .utils import search_halls, paginate_halls
# Create your views here.


def halls(request):
    search_query, halls = search_halls(request)

    number_of_objects_per_page = 3
    
    paginated_page = paginate_halls(request,halls, number_of_objects_per_page)

    context = {'halls': paginated_page, 'search_query': search_query}
    return render(request, 'halls.html', context)


def single_hall(request, pk):
    hall = Hall.objects.get(pk=pk)  # get single hall
    # get all schedule where these hall been booked
    hall_schedules = MainSchedule.objects.filter(pre_schedule__hall=hall)

    context = {'hall': hall, 'hall_schedules': hall_schedules}

    return render(request, 'single-hall.html', context)


def createHall(request):
    form = HallForm()
    
    current_path = request.get_full_path()
    try:

        if request.method == "POST":
            form = HallForm(request.POST, request.FILES)
            if form.is_valid():
                hall_form = form.save(commit=False)
                hall_form.name = hall_form.name.upper()

                form.save()
                message = 'You have successfully added a new hall.'
                messages.success(request, message)
                return redirect('/')
    except ValidationError as e:
        message = e
        messages.error(request,message)
        return redirect(current_path)

    context = {'form': form}
    return render(request, 'add-hall-form.html', context)


def deleteHall(request, pk):

    hall = Hall.objects.get(pk=pk)

    if request.method == 'POST':

        hall.delete()
        message = 'You have succefully delete a hall.'
        messages.success(request, message)
        return redirect('/')

    context = {'hall': hall}
    return render(request, 'delete-hall.html', context)

