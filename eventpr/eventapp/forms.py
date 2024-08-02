from django import forms
from . models import Online, Contact

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Online
        fields='__all__'

        widgets={
            'datetime': DateTimeInput(),
        }

        labels={
            'cus_name':"Customer Name:",
            'cus_ph':"Customer Phone:",
            'email':"email:",
            'address':"Your Current Address",
            'datetime':"Date and Time",
            'name':"Venue Name:",
            'type':"Event Type",
            'guest' : "Guests Expected:",
            'budget':"Budget",
            'service':"Any Preference on Service: ",
            'request':"Any request:",

        }
class ContactUs(forms.ModelForm): 
    class Meta:
        model=Contact
        fields='__all__'

        labels={
            'c_name':"Customer Name:",
            'c_email':"Customer Email:",
            'subject':"Subject:",
            'message':"Message",
     }   
