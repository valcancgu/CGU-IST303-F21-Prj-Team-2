from django.shortcuts import render
from db.models import DBService

# Create your views here.
def index(request):
    services = DBService.objects.all()
    return render(request, 'service_menu/menu.html', {'services': services})
