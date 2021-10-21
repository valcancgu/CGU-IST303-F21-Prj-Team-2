from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField, DateTimeField
from datetime import datetime, time

class SignupForm(forms.Form):

    username = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()

        



        #if cc_myself and subject and "help" not in subject:
            # msg = "Must put 'help' in subject when cc'ing yourself."
            # self.add_error('cc_myself', msg)
            # self.add_error('subject', msg)
