from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator
from pagination import settings

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        new_dict = []
        x= {}
        #i = 0
        for row in reader:
            x['Name'] = row['Name']
            x['Street'] = row['Street']
            x['District'] = row['District']
            new_dict.append(x)
            x = {}
            #i += 1
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(new_dict, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
    }
    return render(request, 'stations/index.html', context)
