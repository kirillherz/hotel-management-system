from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

class SelectDateForm(forms.Form):
    date_in = forms.DateField()
    date_out = forms.DateField()

def listRooms(request):
    sql = """
SELECT 
     management_room.number, management_room.id,
     management_tariff.name as tarrif_name, management_tariff.units as units,
     management_valuta.name as valuta_name, management_valuta.abbreviation as valuta_abbreviation
from 
    management_room, 
    management_tariff,
    management_valuta
where 
     management_room.id IS NOT (SELECT management_record.room_id from management_record where
     management_record.date_in > %s and management_record.date_out < '2018-01-01' )
and 
     management_tariff.id = management_room.tariff_id
and 
     management_valuta.id = management_tariff.valuta_id
             """
    form = SelectDateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():   
        date_in = form.cleaned_data['date_in']
        date_out = form.cleaned_data['date_out']
        rooms = Room.objects.raw(sql,[date_in])
    else:
        rooms = None
    return render(request, 'list_rooms.html',{
                                               'form' : form,
                                               'rooms': rooms,
                                              })
    
    
    
