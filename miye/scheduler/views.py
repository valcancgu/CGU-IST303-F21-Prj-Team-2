from django.shortcuts import render
from django.http import HttpResponseRedirect

from db.models import DBService, DBGuest, DBAppointment
from .forms import ScheduleForm, is_time_between
from datetime import datetime, timedelta

from itertools import chain

def timeslot_is_free(service, date, time):
    print(service)
    print(type(date))
    d = datetime.strptime(date, '%Y-%m-%d')
    print(type(d))
    print(time)
    t = datetime.strptime(time, '%H:%M:%S').time()
    print(type(time))
    print('\n\n')

    try:
        appointments = DBAppointment.objects.filter(date=d)
    except Exception as e:
        print(e)
        print('found no appointments on that date')
        appointments = None

    if appointments is None:
        return True

    try:
        for appointment in appointments:
            """
            [(0, "Mineral Bath: 90 mins – $2.50 per minute"),
              (1, "Mineral Bath: 60 mins – $2.50 per minute"),
              (2, "Swedish Massage: 30 mins – $3.00 per minute"),
              (3, "Swedish Massage: 60 mins – $3.00 per minute"),
              (4, "Deep Tissue: 30 mins – $3.00 per minute"),
              (5, "Deep Tissue: 60 mins – $3.00 per minute"),
              (6, "Shiatsu: 30 mins – $3.00 per minute"),
              (7, "Shiatsu: 60 mins – $3.00 per minute")]
            """
            # is it the same service?
            if service == appointment.service:

                duration = [
                    90,
                    60,
                    30,
                    60,
                    30,
                    60,
                    30,
                    60
                ]

                end_time = appointment.start_time + timedelta(minutes = duration[service])
                if is_time_between(appointment.start_time, end_time, t):
                    continue
                else:
                    return False

    except TypeError as te:
        print(te)
        print('only one appointment in the system, try again')

    return True
# Create your views here.
def index(request):
    # services = DBService.objects.all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ScheduleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if timeslot_is_free(form['service'].value(), form['date'].value(), form['time'].value()):
                """
                guest = DBGuest.objects.filter(id=form['spa_number'].value())

                appt = DBAppointment(service=form['service'].value(),
                     date=form['date'].value(), start_time=form['time'].value())

                appt.save()

                appt.guests.add(guest.id)

                appt.save()
                """
                spa_numbers = form['spa_number'].value()

                lookup_numbers = []

                for number in spa_numbers.split(','):
                    lookup_numbers.append(int(number))

                guests = []

                for number in lookup_numbers:
                    try:
                        guest = DBGuest.objects.get(id=number)
                        guests.append(guest)
                    except Exception as e:
                        return HttpResponseRedirect('/no_guest')

                appt = DBAppointment.objects.create(
                    service=form['service'].value(),
                    date=form['date'].value(),
                    start_time=form['time'].value()
                )

                for guest in guests:
                    guest.appointments.add(appt)

                # receive_user = User.objects.get(id=user_id)

                # print(guest.appointments.all())
                #
                # appt.guests.add(guest)


                # message = Message.objects.create(
                    # title=title,
                    # content=content,
                    # create_user=create_user,
                    # receive_user=receive_user,
                # )
                # message.save() - no needs in save() when you use create() method
                # message.receive_user.add(receive_user)

                return HttpResponseRedirect('/calendar')

            else:
                return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScheduleForm()

    services = DBService.objects.all()
    return render(request, 'scheduler/schedule.html', {'form': form, 'services': services})

def no_guest(request):
    return render(request, 'scheduler/no-guest.html')


def calendar(request):
    appointments = DBAppointment.objects.order_by('date', 'start_time')
    guests = DBGuest.objects.all()
    #print(appointments.guests)
    print(appointments[0].dbguest_set.all())
    display_list = []

    for appt in appointments:
        display_list.append({
            'service': appt.service,
            'date': appt.date,
            'start_time': appt.start_time,
            'guests': list(appt.dbguest_set.all())
        })

    return render(request, 'scheduler/calendar.html', {'display_list': display_list, 'appointments': appointments, 'guests': guests})
