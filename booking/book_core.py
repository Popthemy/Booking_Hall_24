
'''Purpose of these function is to make sure a class isn't booked in the middle of a class'''

MIN_TIME, MAX_TIME = 7, 19



def dynamic_time_choices(start_end):
    ''' Getting dynamic time choices,  
    param: start_end - this is either a tuple or list of queryset containing the start and end time of each courses for the class for a particular day.
    return: if the queryset is empty then all time is availble at that moment TIME_CHOICES 
    else return avail and unavail which avail is needed by the field as the time choice and 
    unavails needed to check for conflict inside of our views or signal to make sure that the time user choose doesn't span in the middle of a class .'''


    # total range of time for a day
    TIME_CHOICES = [(H, f'{H-12}:00 PM') if H > 12 else (H, f'{H}:00 AM') for H in range(MIN_TIME , MAX_TIME)]

    # total duration of already booked classes gotten from start_end, since when a class ends a class can start we don't need the stop time
    unavailable_time = set( )

    if not start_end :
        return TIME_CHOICES, unavailable_time

    unavailable_time = { time for start,end in start_end for time in range(start,end) }

    # to get available time based on the previous time in our Db
    available_time = [ choices for choices in TIME_CHOICES if choices[0] not in unavailable_time ]

    return available_time, unavailable_time


# value list of the start and end time of each class respective to a particular hall.
# if this list happen to be empty then then all the TIme choices should be the result
# start_end = ()


def course_span_conflict(starts, ends, start_end):
    '''This function is needed after user have picked their time from list of available time.
    param: starts - the start_time of main_schedule
    param: ends - the end_time of main_schedule
    param: unavailable_time - filter the main_schedule by hall, date to return values_list(start_time, end_time)'''

    unavailable_time  = { time for start,end in  start_end for time in range(start,end) }
    
    span_conflict =  any( time in unavailable_time  for time in range(starts, ends)) # return false if all are false 

    return span_conflict
     
    

# start , end = 12, 13
  