from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.forms import ModelForm

class SelectDateForm(forms.Form):
    date_in = forms.DateField(label = 'Дата въезда')
    date_out = forms.DateField(label = 'Дата выезда')

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

    def series_validator(value):
        if len(str(value)) != 4:
            raise forms.ValidationError('invalid', code = 'invalid')

    passport_series = forms.IntegerField(label = 'Cерия паспорта', validators = [series_validator],error_messages = {'invalid' : 'Некоректная серия'})

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
                  'date_out',]

      
    
def record(request, id_room = None):
    room = Room.objects.get(pk = id_room)
    total = room.tariff.units
    record = Record(room = room, total = total)
    form = RecordForm(request.POST or None, instance = record)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("Клиент успешно зарегистрирован!")
    return render(request, 'register.html', {'form' : form})

class PaymentForm(ModelForm):
    class Meta:
        model = Additional_payment
        fields = '__all__'
    
def add_payment(request):
    form = PaymentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        record = form.cleaned_data['record']
        record.total += form.cleaned_data['service'].price * form.cleaned_data['size']
        record.save()
        form.save()
        return HttpResponse('Платеж добавлен')
    return render(request, 'add_payment.html', {'form' : form})

class BillForm(forms.Form):
    record = forms.ModelChoiceField(label = 'Клиент', queryset = Record.objects.all())
    
def bill(request):
    form = BillForm(request.GET or None)
    if request.method == 'GET' and form.is_valid():
        record = form.cleaned_data['record']
        payments = Additional_payment.objects.filter(record = record)
        total = record.total
        room_price = record.room.tariff.units
        return render(request, 'bill.html', {'room_price' : room_price,'form':form, 'total' : total, 'payments' : payments})
    return render(request,'bill.html',{'form':form})
    
    
    
    
    

