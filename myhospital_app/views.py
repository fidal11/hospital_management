from django.shortcuts import render,redirect
from admin_app .models import Admin
from doctor.models import Doctor
from django.core.mail import send_mail
from staff.models import Staff
from django.http import JsonResponse
from .models import Patient,Booking
from patient .models import Slots
from admin_app .models import Departments
from django.conf import settings
import random
from django.core.exceptions import ValidationError  
from datetime import datetime

# Create your views here.

def master(request):
    return render(request,'myhospital_app/master.html')

def login(request):
    msg = ''
    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        password = request.POST['password']
        
        try:
            patient = Patient.objects.get(email=patient_id,password=password)
            request.session['patient']=patient.id
            return redirect('patient:home')
        except:
            msg= 'Incorrect Username Or Password'
    else:
        msg='error'        
    return render(request,'myhospital_app/login.html')

def booking(request):
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
        
    return render(request,'myhospital_app/booking.html',{'doctor':doctor,'departments':departments,'slots':slots})
def home(request):
    doctor=Doctor.objects.all()
    return render(request,'myhospital_app/home.html',{'doctor':doctor})

def demo(request):
    return render(request,'myhospital_app/demo.html')

def patient_portal(request):
    msg = ''
    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        password = request.POST['password']
        
        try:
            patient = Patient.objects.get(email=patient_id,password=password)
            request.session['patient']=patient.id
            return redirect('patient:home')
        except:
            msg= 'Incorrect Username Or Password'
    else:
        msg='error'        
    return render(request,'myhospital_app/patient_portal.html')

def staff_login(request):
    msg = ''
    if request.method == 'POST':
        staff_id = request.POST['staff_id']
        password = request.POST['password']
        
        try:
            staff = Staff.objects.get(staffid=staff_id,password=password)
            request.session['staff']=staff.id
            return redirect('staff:master')
        except:
            msg= 'Incorrect Username Or Password'
    
    return render(request,'myhospital_app/staff_login.html')

def doctor_login(request):
    msg = ''
    if request.method == 'POST':
        doctor_id = request.POST['doctor_id']
        password = request.POST['password']
        
        try:
            doctor = Doctor.objects.get(doctorid= doctor_id,password=password)
            request.session['doctor']=doctor.id
            return redirect('doctor:home')
        except:
            msg= 'Incorrect Username Or Password'
    return render(request,'myhospital_app/doctor_login.html')

def admin(request):
    msg=''
    if request.method=='POST':
        user_name =request.POST['username']
        password = request.POST['password']

        try:
            admin = Admin.objects.get(user_name = user_name , password = password)
            request.session['admin']= admin.id
            return redirect('admin_app:home')
        
            
        except:
            msg='Incorrect Username or password'

    
    return render(request,'myhospital_app/admin_login.html',{'message':msg})

def about_us(request):
    return render(request,'myhospital_app/about_us.html')

def contact(request):
    return render(request,'myhospital_app/contact.html')


def get_doctors(request):
    department_id = request.GET.get('department_id')
    doctors = Doctor.objects.filter(department_id=department_id)
    doctor_list = [{'id': doctor.id, 'name': doctor.name} for doctor in doctors]
    return JsonResponse(doctor_list, safe=False)


 

def get_day(request):
    doctor_id=request.GET['doctor_id']
    days = Slots.objects.filter(doctor_id = doctor_id)
     
    
    day_list = [{'id':slot.id,'day':slot.day}for slot in days]
    return JsonResponse(day_list, safe=False)
    
def get_time(request):
    slots_id = request.GET['slots_id']
    time = Slots.objects.filter(id=slots_id).values('time')
    time_list = [{'time': slot['time']} for slot in time]
    return JsonResponse(time_list, safe=False)


def patient_register(request):
    mail = ''
    msg = ''
    if request.method == 'POST':
        patient_name = request.POST['name']
        patient_age = request.POST['age']
        patient_dob = request.POST['dob']
        patient_gender = request.POST['gender']
        patient_mobile = request.POST['phone']
        patient_mail = request.POST['email']
        patient_place = request.POST['place']
        mobile_exists = Patient.objects.filter(phone = patient_mobile).exists()
        
        if not mobile_exists:
            new_patient= Patient(
                name=patient_name,
                age=patient_age,
                dob=patient_dob,
                gender=patient_gender,
                phone=patient_mobile,
                email=patient_mail,
                place=patient_place
            )
            new_patient.save()
            
            mail='uour id '+str(patient_mail)+'and password is '+'12345678'
            msg ='Registered Successfully'
            send_mail(
                'You have been successfully registerd' ,
                mail,
                settings.EMAIL_HOST_USER,
                [new_patient.email]
            )
    else:
        msg='Error'
        
        
        
    return render(request,'myhospital_app/patient_register.html')