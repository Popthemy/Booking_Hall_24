from django import forms
from .models import Pre_Schedule, Main_Schedule
from .book_core import dynamic_time_choices

class Pre_ScheduleForm(forms.ModelForm):
    class Meta:
        model = Pre_Schedule
        fields = ['course', 'date']  # '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'format':  'yyyy-mm-dd', 'type': 'date', }),
            'course': forms.DateInput(attrs={'placeholder':  'Enter course code' }),
        } # changing the type of date field from text to date ad specying formats

class Main_ScheduleForm(forms.ModelForm):
    class Meta:
        model = Main_Schedule
        fields = '__all__'
        exclude = [ 'pre_schedule']

        widgets = {
            'course_information': forms.DateInput(attrs={ 'type': 'textarea' , 'placeholder':  'Enter information to tag with this booking i.e assignment , test coming up or ....' }),
        } # changing the type of date field from text to date ad specying formats

    def __init__( self, *args, pre_schedule=None, **kwargs):
        # overwritimg the time_choices field
        super().__init__(*args, **kwargs)
        if pre_schedule:
            # get the hall, date and query the mainschedule and get the start and end time back in temple
            pre_schedule_hall = pre_schedule.hall
            pre_schedule_date  = pre_schedule.date

            main_schedule = Main_Schedule.objects.filter(pre_schedule__hall=pre_schedule_hall, pre_schedule__date=pre_schedule_date)
            start_end = [ (schedule.start_time,  schedule.end_time) for schedule in  main_schedule ]

            # available_time, unavailable_time
            if start_end:
                # if there was no booked time before then the list is empty  and this won't execute
                available_time, unavailable_time = dynamic_time_choices(start_end=start_end)
                self.fields['start_time'].choices = available_time
                self.fields['end_time'].choices = available_time


            print(f'the main schedule {start_end}, {pre_schedule_hall}, {pre_schedule_date}')
            