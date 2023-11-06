from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.core.exceptions import ValidationError  

from myhospital_app .models import Booking , Patient
from admin_app .models import Departments
from doctor.models import Doctor
from .models import Slots

# Create your views here.

def master(request):
    # patient = Patient.objects.filter(id = request.session['patient']).values('name')
    
    patient = Patient.objects.get(id = request.session['patient'])
     
    return render(request,'patient/master.html' , {'patient':patient})

def home(request):
    patient = Patient.objects.get(id = request.session['patient'])

    patient_id = request.session['patient']
    
     
    
    recent_booking = Booking.objects.filter(patient_id=patient_id).order_by('-id')[0:1]
    
    return render(request,'patient/home.html',{'booking':recent_booking,'patient':patient})

 

def appoinments(request):
    patient = Patient.objects.get(id = request.session['patient'])
    
    return render(request,'patient/appoinments.html',{'patient':patient})

def logout(request):
    del request.session['patient']
    request.session.flush()
    return redirect( 'myhospital_app:home')

 
def new_booking(request):
    patient = Patient.objects.get(id = request.session['patient'])
    doctor = Doctor.objects.all()
    departments = Departments.objects.all()
    slots = Slots.objects.all()
    msg = ''
    mail=''
    if request.method =='POST':
        patient_name = request.POST['name']
        patient_age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        selected_department = request.POST['department']
        selected_doctor = request.POST['doctor']
        slot_day = request.POST['day-select']
        slot_time = request.POST['time-select']
        patientId = request.POST['patientId']
        
        booking = Booking(
            name = patient_name,
            age = patient_age,
            gender = gender,
            phone = phone,
            email = email,
            department_id = selected_department,
            doctor_id = selected_doctor,
            slot_id = slot_day,
            slotTime = slot_time,
            patient_id=patientId,
             
        )
        booking.save() 
        msg='Appoinment registered succesfully'
        mail='Your Appoinment for the day '+str(slot_day)+ ' in MyHospital with '+selected_doctor+' at '+str(slot_time)+  ' has been Registered Successfully'
        msg ='Registered Successfully'
        send_mail(
            'Welcome to MyHospital ' ,
            mail,
            settings.EMAIL_HOST_USER,
            [booking.email]
        )
        
    else:
        msg='Appoinment Not done'
        
    return render(request,'patient/new_booking.html',{'doctor':doctor,'departments':departments,'slots':slots,'patient':patient})
 
 
 
def appoinment_list(request):
    # getting the logged in patients id 
    
    patient_id = request.session['patient']
    
    bookings = Booking.objects.filter(patient_id=patient_id)
     
    return render(request,'patient/appoinment_list.html',{'bookings':bookings})

def change_password(request):
    msg = ''
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if new_password == confirm_password:
            
            if len(new_password) >= 8:


                patient = Patient.objects.get(id= request.session['patient'])

                if patient.password == current_password:

                    Patient.objects.filter(id= request.session['patient']).update(password = confirm_password)
                    
                    msg = 'Password changed succesfully'
                else:
                    msg = 'Invalid password'
            else:
                msg = 'password should be min 8 characters'
        else:
            msg = 'password does not match'

    return render(request,'patient/change_password.html',{'msg':msg})


def prescriptions(request):
    patient_id= request.session['patient']
    bookings = Booking.objects.filter(patient_id=patient_id)
    
    return render(request,'patient/prescriptions.html',{'booking':bookings})

def view_prescription(request,bid):
    booking = Booking.objects.get(id = bid)
    
    return redirect('patient:appoinment_list')