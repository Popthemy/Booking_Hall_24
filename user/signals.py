from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User

from django.dispatch import receiver
from .models import RepProfile


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