from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

class SelectDateForm(forms.Form):
    date_in = forms.DateField()
    date_out = forms.DateField()

def listRooms(request):
    sql = """SELECT * from management_room
             where management_room.id IS NOT
             (SELECT management_record.room_id from management_record where
             management_record.date_in > %s and management_record.date_out < %s )"""
    form = SelectDateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():   
        date_in = form.cleaned_data['date_in']
        date_out = form.cleaned_data['date_out']
        rooms = Room.objects.raw(sql,[date_in,date_out])
    else:
        rooms = None
    return render(request, 'list_rooms.html',{
                                               'form' : form,
                                               'rooms': rooms,
                                              })
    
    
    
