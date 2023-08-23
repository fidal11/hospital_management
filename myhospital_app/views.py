from django.shortcuts import render,redirect
from admin_app .models import Admin
from doctor.models import Doctor
from django.core.mail import send_mail
from staff.models import Staff
from django.http import JsonResponse
from .models import Patient
from admin_app .models import Departments
from django.conf import settings
import random
from django.core.exceptions import ValidationError  

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
            return redirect('patient:master')
        except:
            msg= 'Incorrect Username Or Password'
    else:
        msg='error'        
    return render(request,'myhospital_app/login.html')

def register(request):
    doctor = Doctor.objects.all()
    departments = Departments.objects.filter(specialisation='doctor')
    msg = ''
    mail=''
    if request.method =='POST':
        patient_name = request.POST['name']
        patient_age = request.POST['age']
        dob = request.POST['dob']
        gender = request.POST['gender']
        place = request.POST['place']
        phone = request.POST['phone']
        email = request.POST['email']
        selected_department = request.POST['department']
        selected_doctor = request.POST['doctor']
        date = request.POST['date']
        password = random.randint(5555,9999)
        
        appoinment = Appoinment(
            name = patient_name,
            age = patient_age,
            dob = dob,
            gender = gender,
            place = place,
            phone = phone,
            email = email,
            department_id = selected_department,
            doctor_id = selected_doctor,
            date_of_appoinment = date,
            password=password,
             
        )
        appoinment.save() 
        msg='Appoinment registered succesfully'
        mail='Your Appoinment for the date '+str(date)+ ' in MyHospital with '+selected_doctor+  ' has been Registered Successfully'
        msg ='Registered Successfully'
        send_mail(
            'Welcome to MyHospital ' ,
            mail,
            settings.EMAIL_HOST_USER,
            [appoinment.email]
        )
        
    else:
        msg='Appoinment Not done'
        
    return render(request,'myhospital_app/register.html',{'doctor':doctor,'departments':departments})
def home(request):
    doctor=Doctor.objects.all()
    return render(request,'myhospital_app/home.html',{'doctor':doctor})

def demo(request):
    return render(request,'myhospital_app/demo.html')

def patient_portal(request):
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




 