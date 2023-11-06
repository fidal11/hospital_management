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
from patient.models import Slots


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
    departments = Departments.objects.all()
    mail = ''
    msg=''
    if request.method =='POST':
        doctor_name = request.POST['name']
        doctor_age = request.POST['age']
        department = request.POST['department']
        qualification = request.POST['qualification']
        doctor_id = random.randint(1111,4444)
         
        email = request.POST['email']
        mobile_no = request.POST['mobile']
        image = request.FILES['image']
        
        new_doctor = Doctor(
            name = doctor_name,                                         
            age = doctor_age,
            department_id = department,
            qualification = qualification,
            doctorid = doctor_id,
             
            email = email,
            mobile = mobile_no,
            image = image
        )
        new_doctor.save()
        
        # sending mail to registred user
        
        mail='uour id '+str(doctor_id)+'and password is '+'12345678'
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
    department = Departments.objects.all()
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
    return render(request,'admin_app/doctor_records.html',{'doctors':doctor})

def staff_rec(request):
    staff = Staff.objects.all()
    return render(request,'admin_app/staff_records.html',{'staff':staff})

def departments(request):
    dep = Departments.objects.all()
    msg=''
    if request.method =='POST':
        dep_name = request.POST['department_name']
        
        image = request.FILES['image']
        dep_exists = Departments.objects.filter(name=dep_name).exists()
        if not dep_exists:
            new_department = Departments(
                name = dep_name,
                image = image
            
                
            )
            new_department.save()
            msg = 'Added Succesfully'
        else:
            msg='Department Already Exists'
    return render(request,'admin_app/department.html',{'msg':msg,'dep':dep})

def appoinments(request):
    appoinment = Patient.objects.filter(status='pending') 
    return render(request,'admin_app/appoinments.html',{'appoinments':appoinment})

def slot(request):
    doctor = Doctor.objects.all()
    return render(request,'admin_app/slot.html',{'doctors':doctor})

def view_slots(reuqest,d_id):
    doctors = Doctor.objects.get(id=d_id)
    slot = Slots.objects.filter(doctor=doctors)
    
    
    return render(reuqest, 'admin_app/view_slots.html',{'doctor':doctors,'slot':slot})

#adding slots to doctor
def slot_managment(request, d_id):
    msg = ''
    doctor = Doctor.objects.get(id=d_id)
    
    if request.method == 'POST':
        day = request.POST['day']
        from_time = request.POST['from_time']
        to_time = request.POST['to_time']
        time_range = f"{from_time}-{to_time}"  #f-strings(formatted strings) to concatenate the 'from_time' and 'to_time' values with a hyphen '-' in between them.
        
        existing_slot = Slots.objects.filter(doctor=doctor, day=day, time=time_range).first()

        if existing_slot:
            msg = 'Slot already exists.'
        else:
            new_slot = Slots(doctor=doctor, day=day, time=time_range)
            new_slot.save()
            msg = 'Slot added successfully'
        
             
         
        
    return render(request, 'admin_app/slot_managment.html', {'doctor': doctor, 'msg': msg})

def delete_slot(reuqest,s_id):
    try:
    
        slot = Slots.objects.get(id = s_id) 
        slot.delete()   
        
        return redirect('admin_app:view_slots')
    
    except Slots.DoesNotExist:
        
        pass


def doctor_profile(request, d_id):
    doctors = Doctor.objects.get(id=d_id)
    return render(request,'admin_app/doctor_profile.html',{'doctor':doctors})

# def doctor_satus_update(request,Did):
     
#     doctor = Doctor.objects.get(id=Did)
#     doctor.status='on leave'
#     doctor.save()
#     msg ='Dr'+str(doctor.name)+' You are kindly removed of your Duty in MyHospital.We Thankyou for your service'
#     send_mail(
#             subject = 'Your account was Approved',
#             message = msg,
#             from_email = 'msfidal2001@gmail.com',
#             recipient_list = [doctor.email]
            
#         )
#     return redirect('admin:doc_records')

def remove_doctor(request, Did):
    try:
        doctor = Doctor.objects.get(id=Did)
        doctor_name = doctor.name
        doctor_email = doctor.email
        doctor.delete()
        
        msg = f'Dr {doctor_name}, you have been removed from MyHospital. Thank you for your service.'

        send_mail(
            subject='Doctor Removal Notification',
            message=msg,
            from_email='msfidal2001@gmail.com',
            recipient_list=[doctor_email]
        )

        return redirect('admin_app:doc_records')
    except Doctor.DoesNotExist:
        # Handle the case where the doctor with the provided ID does not exist.
        # You can customize this error handling according to your needs.
        pass