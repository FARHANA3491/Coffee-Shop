from django import forms
from .models import booking
from django.forms.widgets import TimeInput, TextInput
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
    input_type='date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class BookingForm(forms.ModelForm):
    cust_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Customer Name"}),label="Customer Name")
    cust_mail = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Customer Email"}),label="Customer Email")
    cust_date = forms.DateField(widget=forms.DateInput(attrs={'class':"form-control",'type':"date"}),label="Customer Date")
    cust_time = forms.TimeField(widget=forms.TimeInput(attrs={'class':"form-control",'type':"time"}),label="Customer Time")
    cust_pers = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"Number of person"}),label="Number of person")
    class Meta:
        model=booking
        fields='__all__'
        widgets={
            'cust_date':DateInput(),
            'cust_time':TimeInput(format='%H:%M'),
        }
        labels = {
            'cust_name' : "Customer Name",
            'cust_mail' : "Customer Email",
            'cust_date' : "Booking Date",
            'cust_time' : "Bookimg Time",
            'cust_pers' : "Number of Person",
        }
        
    # def clean_booking_time(self):  FOR CHECKING BOOKING TIME IS NOT BOOKED BY ANOTHER PERSON
    #         booking_time = self.cleaned_data['cust_time']
    #         existing_bookings = booking.objects.filter(cust_time=booking_time)

    #         if existing_bookings.exists():
    #             raise ValidationError("This time is already booked. Please choose a different time.")

    #         return booking_time