from .models import DefaultRepList 



def rep_status(request,form):
    '''This function makes sure a user isn't marked as a rep if he isn't not actually a rep.
    All reps details are found in the Default Rep list so if a user details doesn't belongs there 
    the person is not a rep'''
    email = form.email

    return DefaultRepList.objects.filter(email=email).exists()
    