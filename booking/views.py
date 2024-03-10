from django.shortcuts import render, redirect
from building.models import Hall
from .models import MainSchedule, PreSchedule
from .forms import PreScheduleForm, MainScheduleForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login-rep')
def create_preSchedule(request, pk):
    hall = Hall.objects.get(pk=pk)
    form = PreScheduleForm()

    if request.method == "POST":

        form = PreScheduleForm(request.POST)

        if form.is_valid():
            pre_schedule_form = form.save(commit=False)

            # filling the hall field
            pre_schedule_form.hall = hall

            pre_schedule_form.save()
            message = 'First process completed. Fill the next form to be assured of your schedule'
            messages.info(request, message)

            return redirect('main-schedule', pre_schedule_form.id)

    context = {'hall': hall, 'form': form}
    return render(request, 'pre-schedule-form.html', context)




@login_required(login_url='login-rep')
def create_mainSchedule(request, pk):
    schedule_owner = request.user.repprofile

    pre_schedule = PreSchedule.objects.get(pk=pk)

    current_url = request.get_full_path()  # for redirection inccase of error

    # constructor require pre_schedule it must be passed in to generate dynamic time
    form = MainScheduleForm(pre_schedule=pre_schedule)
    try:
        if request.method == 'POST':
            form = MainScheduleForm(request.POST, pre_schedule=pre_schedule)

            if form.is_valid():
                main_schedule_form = form.save(commit=False)
                
                main_schedule_form.rep_profile = schedule_owner
                main_schedule_form.pre_schedule = pre_schedule
                main_schedule_form.save()

                message = 'Schedule successfull!. Find your schedule among the list of schedules.'
                messages.success(request, message)
                
                return redirect('single-hall', pk=pre_schedule.hall.id)

    except ValidationError as e:
        message = e
        messages.error(request, message)
        return redirect(current_url)

    context = {'pre_schedule': pre_schedule, 'form': form}
    return render(request, 'main-schedule-form.html', context)


@login_required(login_url='login-rep')
def editPreSchedule(request,pk):
    page = 'editing'
    
    pre_schedule = PreSchedule.objects.get(pk=pk)
    form = PreScheduleForm(instance=pre_schedule)
    if request.method == 'POST':
        form = PreScheduleForm( request.POST, instance=pre_schedule)
        if form.is_valid():
            form.save()
            message = 'Complete your editing on the next form. '
            messages.info(request,message)
            return redirect('edit-mainschedule', pk=pre_schedule.pk)

    context = {'form': form, 'page': page}
    return render(request, 'pre-schedule-form.html', context)


@login_required(login_url='login-rep')
def editMainSchedule(request,pk):
    page = 'editing'

    pre_schedule = PreSchedule.objects.get(pk=pk)
    current_url = request.get_full_path() # for redirecting in case of errors

    # to find instance of main schedule the preschedul belongs to
    main_schedule = MainSchedule.objects.get(pre_schedule=pre_schedule)

    form = MainScheduleForm(instance=main_schedule, pre_schedule=pre_schedule) # pre-filled form and also passing the prescheduled needed for the dynamic timing 
    try:
        if request.method == 'POST':
            form = MainScheduleForm( request.POST, instance=main_schedule)
            if form.is_valid():
                form.save()
                message = 'You have succefully updated your schedule '
                messages.success(request, message)
                return redirect('single-hall', pk=pre_schedule.hall.id)
    except ValidationError as e:
        messages.error(request,e)
        return redirect(current_url)

    context = {'form': form, 'pre_schedule': pre_schedule, 'page':page }
    return render(request, 'main-schedule-form.html', context)


@login_required(login_url='login-rep')
def deleteMainSchedule(request,pk):
    main_schedule = MainSchedule.objects.get(pk=pk)
    
    
    if request.method == 'POST':
   
        if main_schedule:
            main_schedule.delete()
            message = 'Succefully deleted a schedule'
            messages.success(request, message)
            return redirect('dashboard' )
    context = { "schedule" : main_schedule }
    return render(request, "delete-schedule.html", context)
