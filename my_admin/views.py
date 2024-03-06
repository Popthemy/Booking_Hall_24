from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import RepListForm
from .models import DefaultRepList
from django.core.exceptions import ValidationError

# Create your views here.

def admin_add_rep(request):
    page = 'adding'
    admin = request.user.repprofile
    form = RepListForm()

    if request.method == 'POST':
        form = RepListForm(request.POST)
        
        if form.is_valid():
            add_rep = form.save(commit=False)
            add_rep.admin = admin
            add_rep.save()

            message = "Rep have been added succefully!"
            messages.success(request,message)
            return redirect('dashboard')
        
    context = {"form":form, 'page':page}
    return render(request, "admin-add-rep.html", context )

def edit_rep_details(request,pk):
    page = "editting"

    current_url = request.get_full_path()
    rep = DefaultRepList.objects.get(pk=pk)
    

    form = RepListForm(instance=rep)

    try:
        if request.method == 'POST':
            form = RepListForm(request.POST, instance=rep)
            if form.is_valid():
                form.save()
                message = 'You have succefully updated rep details '
                messages.success(request, message)
                return redirect('dashboard')
            
    except ValidationError as e:
        messages.error(request,e)
        return redirect(current_url)
        

    context = {'form': form, 'page':page}
    return render(request, "admin-add-rep.html" , context)


def delete_rep_details(request,pk):

    rep = DefaultRepList.objects.get(pk=pk)

    if request.method == 'POST':
        rep.delete()

        message = 'You have succefully deleted a rep details.'
        messages.success(request, message)
        return redirect('dashboard')

    context = {'rep': rep}
    return render(request, 'delete-rep-details.html', context)


def view_all_reps(request):
    admin = request.user.repprofile

    rep_list = DefaultRepList.objects.filter(admin=admin)



    context = {'Reps_list': rep_list}
    return render(request,"all_reps.html", context)

