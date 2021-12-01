from datetime import datetime

from django.test import TestCase


from scheduler.forms import is_time_between

open = datetime.strptime("8:00:00", "%H:%M:%S").time()
close = datetime.strptime("17:00:00", "%H:%M:%S").time()
chk_time = datetime.strptime("10:00:00", "%H:%M:%S").time()


def test_time():
    assert is_time_between(open, close, chk_time) == True



