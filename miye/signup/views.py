from django.shortcuts import render
from db.models import DBGuest

from .forms import SignupForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if timeslot_is_free(form['service'].value(), form['date'].value(), form['time'].value()):
                DBAppointment.objects.create(service=form['service'].value(), guest=form['spa_number'].value(),
                    date=form['date'].value(), start_time=form['time'].value())

                return HttpResponseRedirect('/calendar')

            else:
                return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    guests = DBGuest.objects.all()
    return render(request, 'signup/signup.html', {'form': form, 'guests': guests})
