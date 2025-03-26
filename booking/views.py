from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import auth
import time

def booking_data(request): # To send details for booking
        pickup = request.POST.get('pickup')
        dropoff = request.POST.get('dropoff')
        pickup_date = request.POST.get('pickup_date')
        pickup_time = request.POST.get('pickup_time')
        mobile_number = request.POST.get('number')

        message = f"""
        🚘 New Booking:

        Pickup Location: {pickup}
        Drop-off Location: {dropoff}
        pickup_time: {pickup_time}
        Pickup Date: {pickup_date}
        Mobile Number: {mobile_number}
        """
        send_mail(
            subject='New Booking Request',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['travelsbyguru@gmail.com'],
        )

    
def index(request): # for index page
    if request.method == 'POST':
        booking_data(request)
        return HttpResponseRedirect(f"{reverse('index')}?success=true") 


    accounts = social_accounts.objects.all()
    car_info = cars_details.objects.all()
    success = request.GET.get('success') == 'true'
    return render(request, 'index.html', {'success': success,'accounts': accounts,'car_info': car_info})

def about(request):# for about page
    accounts = social_accounts.objects.all()
    car_info = cars_details.objects.all()
    
    return render(request,'about.html',{'accounts': accounts,'car_info': car_info})

def service(request): # for service page
    accounts = social_accounts.objects.all()
    car_info = cars_details.objects.all()
    
    return render(request,'services.html',{'accounts': accounts,'car_info': car_info})

def contact(request): # for contact page
    accounts = social_accounts.objects.all()
    car_info = cars_details.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('message')

        info = contacts(name=name,email=email,subject=subject,message=msg)
        info.save()

        complaint = f"""
        New Complaint:

        Complaint by: {name}\n
        Email address: {email}\n
        Subject: {subject}\n
        Message: {msg}
        """

        send_mail(
            subject='New Complaint',
            message=complaint,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['travelsbyguru@gmail.com'],
        )

        messages.success(request,'Your complaint has been submitted successfully. We’ll get back to you shortly.')
        return redirect('contact')


    return render(request,'contact.html',{'accounts': accounts,'car_info': car_info})

def reservation(request): # for reservation page
    if request.method == 'POST':

        booking_data(request)

        return HttpResponseRedirect(f"{reverse('reservation')}?success=true") 

    success = request.GET.get('success') == 'true'
    return render(request, 'reservation.html', {'success': success})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.warning(request,'Username is already taken! Try again with different Username.')
            time.sleep(2)
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'Email is already registered! Try again with different Email.')
            time.sleep(2)
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            print('Data saved successfully')
            messages.success(request,'Succesfully registered')
            return redirect('/')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('identifier')
        password = request.POST.get('login_pass')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'Login successful')
            return redirect('/')
        else:
            messages.warning(request,'Invalid credentials! Try again.')
            return redirect('register')
        

def logout(request):
    auth.logout(request)
    time.sleep(3)
    messages.success(request,'Logged out successfully')
    return redirect('/')