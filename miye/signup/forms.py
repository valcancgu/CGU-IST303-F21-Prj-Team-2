from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField, DateTimeField
from datetime import datetime, time

class SignupForm(forms.Form):

    username = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()

        date = cleaned_data.get("date")
        time = cleaned_data.get("time")
        service = cleaned_data.get("service")

        open = datetime.strptime("08:00:00", "%H:%M:%S").time()
        close = datetime.strptime("17:00:00", "%H:%M:%S").time()

        if not is_time_between(open, close, time):
            msg = "WE ARE CLOSED AT THIS TIME"
            self.add_error('date', msg)




        #if cc_myself and subject and "help" not in subject:
            # msg = "Must put 'help' in subject when cc'ing yourself."
            # self.add_error('cc_myself', msg)
            # self.add_error('subject', msg)
