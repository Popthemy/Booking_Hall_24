from django import forms
from .models import PreSchedule, MainSchedule
from .book_core import dynamic_time_choices


class PreScheduleForm(forms.ModelForm):
    class Meta:
        model = PreSchedule
        fields =  '__all__' # ['course', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'format':  'yyyy-mm-dd', 'type': 'date', 'class': 'form-control'}),
            'course': forms.TextInput(attrs={'placeholder':  'Enter course code',  'class': 'form-control'}),
           
        }  # changing the type of date field from text to date ad specying formats

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for name,field in self.fields.items():
            if name == 'hall':
                field.widget.attrs.update({'class':'form-control', 'placeholder':'Shoose hall...'})


def get_dynamic_time_choices(pre_schedule):

    # get the hall, date through querying the mainschedule and get the start and end time back in DB
    pre_schedule_hall = pre_schedule.hall
    pre_schedule_date = pre_schedule.date
    
    try:
        main_schedule_linked_to_pre_schedule = MainSchedule.objects.get(pre_schedule=pre_schedule)
    except MainSchedule.DoesNotExist:
        main_schedule_linked_to_pre_schedule = None

    # main_schedule_linked_to_pre_schedule = main_schedule.objects.get(pre_schedule=pre_schedule)

    main_schedule = MainSchedule.objects.filter(
        pre_schedule__hall=pre_schedule_hall, pre_schedule__date=pre_schedule_date).exclude(pk=main_schedule_linked_to_pre_schedule.pk if main_schedule_linked_to_pre_schedule else None)

    
        
    start_end = [(schedule.start_time,  schedule.end_time)
                 for schedule in main_schedule]
    
    return start_end


class MainScheduleForm(forms.ModelForm):
    class Meta:
        model = MainSchedule
        fields = '__all__'
        exclude = ['pre_schedule', 'rep_profile']

        widgets = {
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

            # print(f'the main schedule {start_end}, {pre_schedule.hall}, {pre_schedule.date}')
