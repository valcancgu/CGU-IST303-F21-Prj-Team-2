from django.shortcuts import render
from db.models import DBGuest
from db.models import DBService
from django.http import HttpResponseRedirect
from .forms import SignupForm
from django.urls import reverse

from scheduler.forms import ScheduleForm

# Create your views here.
def signup(request):

    services = DBService.objects.all()

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_signup = SignupForm(request.POST)



        # check whether it's valid:
        if form_signup.is_valid():
            guest, created = DBGuest.objects.get_or_create(username=form_signup['username'].value())


            return render(request, 'signup/spa_number.html', {'guest': guest})

    # if a GET (or any other method) we'll create a blank form
    else:
        form_signup = SignupForm()

    # guests = DBGuest.objects.all()
    return render(request, 'signup/signup.html', {'form': form_signup})
