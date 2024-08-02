from django.shortcuts import render,redirect
from .models import Venue, Online
from .forms import BookingForm, ContactUs
from django.contrib import messages

# Create your views here.

def index(request):
   # messages.success(request, "Thank you for booking! Your reservation has been confirmed. We look forward to seeing you!")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def venue(request):
    dict_eve={
        'eve':Venue.objects.all()
    }
    return render(request, 'venue.html',dict_eve)

def privacy(request):
    return render(request, 'privacy.html')

def online(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for booking! Your reservation has been confirmed. We look forward to seeing you!")
            return redirect('/')

    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'online.html',dict_form)




def contact(request):
    if request.method=='POST':
        form=ContactUs(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us! We will get back to you soon.")
            return redirect('/')

    form=ContactUs()
    dict_form={
        'form':form
    }
    return render(request,'contact.html',dict_form)

