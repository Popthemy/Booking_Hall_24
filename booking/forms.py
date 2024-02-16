from django import forms
from .models import PreSchedule, MainSchedule
from .book_core import dynamic_time_choices


class PreScheduleForm(forms.ModelForm):
    class Meta:
        model = PreSchedule
        fields = ['course', 'date']  # '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'format':  'yyyy-mm-dd', 'type': 'date', 'class': 'form-control'}),
            'course': forms.TextInput(attrs={'placeholder':  'Enter course code',  'class': 'form-control'}),
        }  # changing the type of date field from text to date ad specying formats


def get_dynamic_time_choices(pre_schedule):

    # get the hall, date and query the mainschedule and get the start and end time back in temple
    pre_schedule_hall = pre_schedule.hall
    pre_schedule_date = pre_schedule.date

    main_schedule = MainSchedule.objects.filter(
        pre_schedule__hall=pre_schedule_hall, pre_schedule__date=pre_schedule_date)
    start_end = [(schedule.start_time,  schedule.end_time)
                 for schedule in main_schedule]
    return start_end


class MainScheduleForm(forms.ModelForm):
    class Meta:
        model = MainSchedule
        fields = '__all__'
        exclude = ['pre_schedule']

        widgets = {
            # 'start_time': forms.TextInput(attrs={'class': 'form-control'}),
            'course_information': forms.Textarea(attrs={'placeholder': 'Enter information to tag with this booking i.e assignment , test coming up or ....', 'class': 'form-control'}),
        }  # changing the type and class of field

    def __init__(self, *args, pre_schedule=None, **kwargs):
        # overwritimg the time_choices field
        super().__init__(*args, **kwargs)
        
        if pre_schedule:
            self.set_time_choices(pre_schedule)

            # available_time, unavailable_time

    def set_time_choices(self, pre_schedule):
        start_end = get_dynamic_time_choices(pre_schedule)
        if start_end:
            # if there was no booked time before then the list is empty and this won't execute
            available_time, _ = dynamic_time_choices(
                start_end=start_end)
            self.fields['start_time'].choices = available_time
            self.fields['end_time'].choices = available_time

            # print(f'the main schedule {start_end}, {pre_schedule_hall}, {pre_schedule_date}')
