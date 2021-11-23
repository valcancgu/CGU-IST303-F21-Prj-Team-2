from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('calendar', views.calendar, name="calendar"),
    path('no_guest', views.no_guest, name="no_guest")

]
