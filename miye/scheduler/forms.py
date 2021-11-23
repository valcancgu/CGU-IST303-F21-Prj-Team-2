from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField, DateTimeField
from datetime import datetime, time

"""
TEST ME: fail if begin_time is before end_time
"""
def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

def is_parseable(spa_number):
    try:
        for number in spa_number.split(','):
            check = int(number)
        return True
    except Exception as e:
        print(e)
        return False

class ScheduleForm(forms.Form):

    #spa_number = forms.IntegerField()
    spa_number = forms.CharField()
    date = DateField(widget = forms.SelectDateWidget())
    time = forms.TimeField()
    print(time)

    CHOICES = [(0, "Mineral Bath: 90 mins – $2.50 per minute"),
              (1, "Mineral Bath: 60 mins – $2.50 per minute"),
              (2, "Swedish Massage: 30 mins – $3.00 per minute"),
              (3, "Swedish Massage: 60 mins – $3.00 per minute"),
              (4, "Deep Tissue: 30 mins – $3.00 per minute"),
              (5, "Deep Tissue: 60 mins – $3.00 per minute"),
              (6, "Shiatsu: 30 mins – $3.00 per minute"),
              (7, "Shiatsu: 60 mins – $3.00 per minute")]

    service = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    def clean(self):
        cleaned_data = super().clean()

        date = cleaned_data.get("date")
        time = cleaned_data.get("time")
        service = cleaned_data.get("service")

        spa_number = cleaned_data.get("spa_number")

        if not is_parseable(spa_number):
            msg = "BAD INPUT FOR SPA NUMBER"
            self.add_error('spa_number', msg)

        open = datetime.strptime("08:00:00", "%H:%M:%S").time()
        close = datetime.strptime("17:00:00", "%H:%M:%S").time()

        if not is_time_between(open, close, time):
            msg = "WE ARE CLOSED AT THIS TIME"
            self.add_error('date', msg)




        #if cc_myself and subject and "help" not in subject:
            # msg = "Must put 'help' in subject when cc'ing yourself."
            # self.add_error('cc_myself', msg)
            # self.add_error('subject', msg)
