from django.shortcuts import render,redirect
from doctor.models import Doctor
from staff.models import Staff
from .models import Admin,Departments
import random
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import F
from .decorator import auth_admin
from myhospital_app .models import Patient


# Create your views here.
@auth_admin
def admin_master(request):
    return render(request,'admin_app/admin_master.html')
@auth_admin
def home(request):
    return render(request,'admin_app/home.html')
@auth_admin
def admin_doctor(request):
    return render(request,'admin_app/admin_doctor.html')

@auth_admin
def add_doctor(request):
    departments = Departments.objects.filter(specialisation = 'doctor')
    mail = ''
    msg=''
    if request.method =='POST':
        doctor_name = request.POST['name']
        doctor_age = request.POST['age']
        department = request.POST['department']
        qualification = request.POST['qualification']
        doctor_id = random.randint(1111,4444)
        password = request.POST['password']
        email = request.POST['email']
        mobile_no = request.POST['mobile']
        image = request.FILES['image']
        
        new_doctor = Doctor(
            name = doctor_name,
            age = doctor_age,
            department_id = department,
            qualification = qualification,
            doctorid = doctor_id,
            password = password,
            email = email,
            mobile = mobile_no,
            image = image
        )
        new_doctor.save()
        
        # sending mail to registred user
        
        mail='uour id '+str(doctor_id)+'and password'+str(password)
        msg ='Registered Successfully'
        send_mail(
            'You have been successfully registerd' ,
            mail,
            settings.EMAIL_HOST_USER,
            [new_doctor.email]
        )
    else:
        msg='Error'
    
    return render(request,'admin_app/add_doctor.html',{'departments':departments})

def staffs(request):
    return render(request,'admin_app/staffs.html')

def staff_reg(request):
    department = Departments.objects.filter(specialisation='staff')
    mail =''
    msg=''
    if request.method =='POST':
        staff_name = request.POST['name']
        staff_age = request.POST['age']
        department = request.POST['department']
        qualification = request.POST['qualification']
        staff_id = random.randint(5555,9999)
        password = request.POST['password']
        email = request.POST['email']
        mobile_no = request.POST['mobile']
        image = request.FILES['image']
        mail_exists = Staff.objects.filter(email = email).exists()
        
        if not mail_exists:
            
            new_staff = Staff(
                name = staff_name,
                age = staff_age,
                department = department,
                qualification = qualification,
                staffid = staff_id,
                password = password,
                email = email,
                mobile = mobile_no,
                image = image
            )
            new_staff.save()
            mail = 'You have Succesfully Appointed your id '+str(staff_id)+'password '+str(password)
            msg ='Registered Successfully'
            send_mail(
                 'Welcome To MY HOSPITAL' ,
            mail,
            settings.EMAIL_HOST_USER,
            [new_staff.email]
            )
        
        else:
            msg='Mail already exists in Database'
    
    return render(request,'admin_app/staff_register.html',{'msg':msg,'department':department})

def logout(request):
    del request.session['admin']
    request.session.flush()
    return redirect( 'myhospital_app:home' )

def doc_records(request):
    doctor = Doctor.objects.all()
    return render(request,'admin_app/doctor_records.html',{'doctor':doctor})

def staff_rec(request):
    staff = Staff.objects.all()
    return render(request,'admin_app/staff_records.html',{'staff':staff})

def departments(request):
    dep = Departments.objects.all()
    msg=''
    if request.method =='POST':
        dep_name = request.POST['department_name']
        specialisation = request.POST['specialisation']
        image = request.FILES['image']
        dep_exists = Departments.objects.filter(name=dep_name).exists()
        if not dep_exists:
            new_department = Departments(
                name = dep_name,
                specialisation=specialisation,
                image = image
            
                
            )
            new_department.save()
            msg = 'Added Succesfully'
        else:
            msg='Department Already Exists'
    return render(request,'admin_app/department.html',{'msg':msg,'dep':dep})

def appoinments(request):
     
    return render(request,'admin_app/appoinments.html')