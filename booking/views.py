from django.shortcuts import render, redirect
from building.models import Hall
from .models import MainSchedule, PreSchedule
from .forms import PreScheduleForm, MainScheduleForm
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your views here.


def create_preSchedule(request, pk):
    hall = Hall.objects.get(pk=pk)
    forms = PreScheduleForm()

    if request.method == "POST":

        forms = PreScheduleForm(request.POST)

        if forms.is_valid():
            pre_schedule_form = forms.save(commit=False)

            # filling the hall field
            pre_schedule_form.hall = hall

            pre_schedule_form.save()
            message = 'First process completed. Fill the next form to be assured of your schedule'
            messages.info(request, message)

            return redirect('main-schedule', pre_schedule_form.id)

    context = {'hall': hall, 'forms': forms}
    return render(request, 'pre-schedule-form.html', context)


def create_mainSchedule(request, pk):
    pre_schedule = PreSchedule.objects.get(pk=pk)

    current_url = request.get_full_path()  # for redirection inccase of error

    # constructor require pre_schedule it must be passed in to generate dynamic time
    forms = MainScheduleForm(pre_schedule=pre_schedule)
    try:
        if request.POST:
            forms = MainScheduleForm(request.POST, pre_schedule=pre_schedule)

            if forms.is_valid():
                main_schedule_form = forms.save(commit=False)
                main_schedule_form.pre_schedule = pre_schedule
                main_schedule_form.save()

                message = 'Schedule successfull!. Find your schedule among the list of schedules.'
                messages.success(request, message)
                # hall/<str:pk>/
                return redirect('single-hall', pk=pre_schedule.hall.id)

    except ValidationError as e:
        message = e
        messages.error(request, message)
        return redirect(current_url)

    context = {'pre_schedule': pre_schedule, 'forms': forms}
    return render(request, 'main-schedule-form.html', context)



def editPreSchedule(request,pk):
    page = 'editing'
    
    pre_schedule = PreSchedule.objects.get(pk=pk)
    forms = PreScheduleForm(instance=pre_schedule)
    if request.POST:
        forms = PreScheduleForm( request.POST, instance=pre_schedule)
        if forms.is_valid():
            forms.save()
            message = 'Complete your editing on the next form. '
            messages.info(request,message)
            return redirect('edit-mainschedule', pk=pre_schedule.pk)

    context = {'forms': forms, 'page': page}
    return render(request, 'pre-schedule-form.html', context)

def editMainSchedule(request,pk):
    page = 'editing'

    pre_schedule = PreSchedule.objects.get(pk=pk)
    current_url = request.get_full_path() # for redirecting in case of errors

    # to find instance of main schedule the preschedul belongs to
    main_schedule = MainSchedule.objects.get(pre_schedule=pre_schedule)

    forms = MainScheduleForm(instance=main_schedule) # pre-filled form
    try:
        if request.POST:
            forms = MainScheduleForm( request.POST, instance=main_schedule)
            if forms.is_valid():
                forms.save()
                message = 'You have succefully updated your schedule '
                messages.success(request, message)
                return redirect('single-hall', pk=pre_schedule.hall.id)
    except ValidationError as e:
        messages.error(request,e)
        return redirect(current_url)


    context = {'forms': forms, 'pre_schedule': pre_schedule, 'page':page }
    return render(request, 'Main-schedule-form.html', context)
