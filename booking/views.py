from django.shortcuts import render, redirect
from building.models import Hall
from .models import Main_Schedule, Pre_Schedule
from .forms import Pre_ScheduleForm, Main_ScheduleForm
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your views here.


def preSchedule(request, pk):
    hall = Hall.objects.get(pk=pk)
    form = Pre_ScheduleForm()

    if request.method == "POST":

        form = Pre_ScheduleForm(request.POST)

        if form.is_valid():
            pre_schedule_form = form.save(commit=False)

            # filling the hall field
            pre_schedule_form.hall = hall

            pre_schedule_form.save()
            message = 'First process completed. Fill the next form to be assured of your schedule'
            messages.info(request, message)

            return redirect('main-schedule', pre_schedule_form.id)

    context = {'hall': hall, 'form': form}
    return render(request, 'pre-schedule.html', context)


def mainSchedule(request, pk):
    pre_schedule = Pre_Schedule.objects.get(pk=pk)

    current_url = request.get_full_path()  # for redirection inccase of error

    # constructor require pre_schedule it must be passed in to generate dynamic time
    form = Main_ScheduleForm(pre_schedule=pre_schedule)
    try:
        if request.POST:
            form = Main_ScheduleForm(request.POST, pre_schedule=pre_schedule)

            if form.is_valid():
                main_schedule_form = form.save(commit=False)
                main_schedule_form.pre_schedule = pre_schedule
                main_schedule_form.save()

                message = 'Schedule successful!. Find your schedule among the list of schedules.'
                messages.success(request, message)
                # hall/<str:pk>/
                return redirect('single-hall', pk=pre_schedule.hall.id)

    except ValidationError as e:
        message = e
        messages.error(request, message)
        return redirect(current_url)

    context = {'pre_schedule': pre_schedule, 'form': form}
    return render(request, 'main-schedule.html', context)
