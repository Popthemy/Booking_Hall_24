from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User

from django.dispatch import receiver
from .models import RepProfile,DefaultRepList


@receiver(post_save, sender=User)
def create_rep_profile(sender, created, instance, **kwargs):
    if created:
        user = instance
        rep_profile = RepProfile.objects.create(
            owner=user,
            username = user.username,
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email
        )


@receiver(post_save,sender=RepProfile)
def update_user_model(sender,created,instance,**kwargs):
    rep_profile= instance
    user = rep_profile.owner
    if not(created):
        user.first_name = rep_profile.first_name
        user.last_name = rep_profile.last_name
        user.username = rep_profile.username
        user.email = rep_profile.email
        user.save()

@receiver(post_delete,sender=RepProfile)
def delete_user(sender,instance,**kwargs):
    rep_profile = instance

    
    try:
        rep = rep_profile.owner
        print(rep)
        rep.delete()
    except:
        pass


@receiver(post_save,sender=DefaultRepList)
def rep_status_confirm_default(sender, created,instance, **kwargs ):
    ''' A signal that toggle the i am a rep button on if a just or edited rep record from the default rep list '''
   
    if created:
        try: 
            rep_profile = RepProfile.objects.get(email=instance.email)
          
            print(rep_profile.i_am_a_rep)
            rep_profile.i_am_a_rep = True
            rep_profile.save()
        except rep_profile.DoesNotExist:
            pass

@receiver(post_delete,sender=DefaultRepList)
def remove_rep_status(sender,instance,**kwargs):

    try:
        rep_profile = RepProfile.objects.get(email=instance.email)
        
        print(rep_profile.i_am_a_rep)
        if rep_profile.i_am_a_rep:
            rep_profile.i_am_a_rep = False
            rep_profile.save()
    except rep_profile.DoesNotExist:
        pass
