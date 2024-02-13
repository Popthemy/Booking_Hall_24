"""Applying constraints accross fields isn't possible so we want to make sure the hall and date from preschedule 
and start_time from Main_schedule is unque
Steps to create the listener:
1. import the pre_save method from models.signal 'from django.db.models.signals import pre_save'
2. import the models needed the sender of the signal (main_schedule) the other model to check its field (pre_schedule)
3. import the receiver decorator 'from django.dispatch import receiver'
usage of receiver '@receiver(method, sender="the model sending the request") 
4. to load the signal go the the app of your apps and add the function to kick start your signal.
"""
from django.db.models.signals import pre_save
from .models import Main_Schedule
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from .book_core import course_span_conflict

@receiver(pre_save, sender=Main_Schedule)
def date_time_hallUnique(sender, instance, **kwargs):
    """The sender is the Main_schedule model cause it's on the save() of this model that this signal is called """
    main_Schedule = instance
    preschedule = main_Schedule.pre_schedule

    # list of field we want to be unique accross our db since mainschedule is a related to pre_schedule we should be able to get it
    hall = preschedule.hall
    date = preschedule.date
    start = main_Schedule.start_time
    end = main_Schedule.end_time

    # Validate time boundaries: 7 <= start < end <= 19
    if not (7 <= start < end <= 19):
        raise ValidationError(
            f'Invalid schedule times: start= {main_Schedule.start_time_display}  must be before end= {main_Schedule.end_time_display} for a valid schedule')

        

    # get the queryset where hall and date match excluding the current saving schedule
    hall_date = Main_Schedule.objects.filter(pre_schedule__hall=hall, pre_schedule__date=date).exclude(pk=main_Schedule.pk if main_Schedule.pk else None)

    # get their start and end time meaning list of when class is aleready scheduled
    booked_time = [ (time_frame.start_time, time_frame.end_time)  for time_frame in hall_date]

    # print(f'This is boooookked time: {booked_time}')
    already_exist = course_span_conflict(starts=start ,ends=end , start_end=booked_time)
    if already_exist:
        raise ValidationError(
            f'There is a class scheduled in between {main_Schedule.start_time_display} to {main_Schedule.end_time_display} at {hall.name} with the specified details before check the sifax hall to see all schedules.')

    conflict_schedules = Main_Schedule.objects.filter(
        pre_schedule__hall=hall, pre_schedule__date=date, start_time=start, end_time=end).exclude(pk=instance.pk if instance.pk else None)

    if conflict_schedules:
        raise ValidationError(
            f'There is a prior schedule for { hall.name } with the specified details before.')

# pre_save.connect(date_time_hallUnique, sender=Main_Schedule)
