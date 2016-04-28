from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.forms import ModelForm

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
      management_record.date_in > %s and management_record.date_out < %s )
    and 
      management_tariff.id = management_room.tariff_id
    and 
      management_valuta.id = management_tariff.valuta_id
             """
    form = SelectDateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():   
        date_in = form.cleaned_data['date_in']
        date_out = form.cleaned_data['date_out']
        rooms = Room.objects.raw(sql,[date_in, date_out])
    else:
        rooms = None
    return render(request, 'list_rooms.html',{
                                               'form' : form,
                                               'rooms': rooms,
                                              })

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['first_name',
                  'middle_name',
                  'last_name',
                  'country',
                  'city',
                  'passport_series',
                  'passport_id',
                  'issued',
                  'date_of_birth',
                  'date_in',
                  'date_out',
                  'room']
    
def record(request, id_room = None):
    room = Room.objects.get(pk = id_room)
    bill = Bill(total = room.tariff.units, date = '1994-06-09')
    bill.save()
    record = Record(room = room, bill = bill)
    form = RecordForm(request.POST or None, instance = record)
    form.fields['room'].initial = id_room
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("Зарегестрирован")
    return render(request, 'register.html', {'form' : form})
    
    
    
    
