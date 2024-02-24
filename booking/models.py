from django.db import models
from building.models import Hall
from user.models import RepProfile
import uuid

# Create your models here.


class PreSchedule(models.Model):

    course = models.CharField(max_length=255)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    date = models.DateField()
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.course

    class Meta:
        ordering = ['date']


class MainSchedule(models.Model):
    # custom time range from 7 to 7
    TIME_CHOICES = [ (H, f'{H-12}:00 PM') if H > 12 else (H, f'{H}:00 AM') for H in range(7, 20) ]

    rep_profile = models.ForeignKey(RepProfile, null=True , on_delete=models.CASCADE )
    pre_schedule = models.OneToOneField(PreSchedule, on_delete=models.CASCADE)
    start_time = models.PositiveIntegerField(
        choices=TIME_CHOICES)  # course begins
    end_time = models.PositiveIntegerField(
        choices=TIME_CHOICES)  # course begins
    course_information = models.TextField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)

    def __str__(self):
        return f'Main: {self.pre_schedule.course} , Date: {self.pre_schedule.date}'
    
    class Meta:
        # should be ordered by the date of preshcedule.
        unique_together = [['pre_schedule', 'start_time']]
        ordering = ['-pre_schedule__date']

    @property
    def start_time_display(self):
        '''The choice field was displaying with a 24hrs formaat was index 0 of our time_choices so we used this function to overwrite it '''
        for choice in self.TIME_CHOICES:
            if choice[0] == self.start_time:
                return choice[1]
        return '0'
    
    @property
    def end_time_display(self):
        for choice in self.TIME_CHOICES:
            if choice[0] == self.end_time:
                return choice[1]
        return '0'