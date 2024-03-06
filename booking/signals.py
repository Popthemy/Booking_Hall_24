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
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from .models import MainSchedule
from .book_core import course_span_conflict

MIN_TIME, MAX_TIME = 7, 19


def validate_schedule_time(instance):
    if not (MIN_TIME <= instance.start_time < instance.end_time <= MAX_TIME):
        raise ValidationError(
            f'Invalid schedule times &#58 start &#61; {instance.start_time_display}  must be before end &#61; {instance.end_time_display} for a valid schedule')


def check_course_span_conflict(instance):

    main_schedule = instance
    preschedule = main_schedule.pre_schedule

    # gets required details for query
    hall = preschedule.hall
    date = preschedule.date
    start = main_schedule.start_time
    end = main_schedule.end_time

    # get the queryset where hall and date match excluding the current saving schedule
    hall_date = MainSchedule.objects.filter(pre_schedule__hall=hall, pre_schedule__date=date).exclude(
        pk=main_schedule.pk if main_schedule.pk else None)

    # get their start and end time meaning list of when class is aleready scheduled
    booked_time = [(time_frame.start_time, time_frame.end_time)
                   for time_frame in hall_date]

    # making sure no ckasses are scheduled btw. the class
    already_exist = course_span_conflict(
        starts=start, ends=end, start_end=booked_time)
    
    if already_exist:
        raise ValidationError(
            f'There is a class scheduled in between {main_schedule.start_time_display} to {main_schedule.end_time_display} at {hall.name} with the specified details before check the sifax hall to see all schedules &#46;')



@receiver(pre_save, sender=MainSchedule)
def date_time_hallUnique(sender, instance, **kwargs):
    """The sender is the Main_schedule model cause it's on the save() of this model that this signal is called """

    # Validate time boundaries: 7 <= start < end <= 19
    validate_schedule_time(instance)

    # gets triggered when there is a conflict
    check_course_span_conflict(instance)

# pre_save.connect(date_time_hallUnique, sender=Main_Schedule)
