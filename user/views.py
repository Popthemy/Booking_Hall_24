from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RepCustomUserForm, RepProfileForm
from booking.models import MainSchedule

# Create your views here.

def create_rep(request):
    page = 'register'
    form = RepCustomUserForm()

    if request.method == "POST":
        form = RepCustomUserForm(request.POST)

        if form.is_valid():
            try:
                rep_instance = form.save(commit=False)
                rep_instance.username = rep_instance.username.strip().capitalize()

                rep_instance.save()
                message = 'Account successfully created!'
                messages.success(request, message)

                login(request, rep_instance)
                return redirect('dashboard')

            except IntegrityError as e:
                message = f"Error creating account: {e}"
                messages.error(request, message)

    context = {'form': form, 'page': page}
    return render(request, 'register-login-rep.html', context)



def login_rep(request):
    page = 'login'
    
    if request.method == 'POST':
        username = request.POST.get('username').strip().capitalize()
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)
        if user:
            login(request, user)
            message = f'Dear {username} welcome back! we have changed somethings since your last visit'
            messages.success(request,message)
            return redirect( request.GET.get('next') if 'next' in request.GET else 'dashboard')
 
        message = 'INVALID PASSWORD! OR INVALID USERNAME!. Please try again.'
        messages.error(request,message)

    context = {'page':page}
    return render(request,'register-login-rep.html', context)



def logout_rep(request):
    message = f'Dear {request.user.username} we are missing you already!! see you around.'
    logout(request)
    messages.success(request,message)
    return redirect('login-rep')




@login_required(login_url='register-rep')
def edit_rep_profile(request):
    rep_profile = request.user.repprofile

    form = RepProfileForm(instance=rep_profile)

    if request.method == "POST":
        form = RepProfileForm(request.POST, instance=rep_profile)

        if form.is_valid():
            try:
                edited_rep_form = form.save(commit=False)
                edited_rep_form.username = edited_rep_form.username.strip().capitalize()

                edited_rep_form.save()
                message = 'Account successfully edited!'
                messages.success(request, message)
                return redirect('dashboard')

            except IntegrityError as e:
                message = f"Error editing account: {e}"
                messages.error(request, message)

    context = {'form': form}
    return render(request, 'rep-profile.html', context)

@login_required(login_url='login-rep')
def rep_dashboard(request):
    rep_profile = request.user.repprofile

    schedules = MainSchedule.objects.filter(rep_profile=rep_profile)
    print(schedules)

    context= {'rep_profile':rep_profile, 'schedules':schedules }
    return render(request, 'dashboard.html', context)
