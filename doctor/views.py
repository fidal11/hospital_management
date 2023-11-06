from django.shortcuts import render,redirect
from .models import Doctor
from django.db.models import F
from myhospital_app.models import Patient,Booking,Prescription


# Create your views here.

def home(request):

    doctors = Doctor.objects.get(id= request.session['doctor'])
    noofpatient= Booking.objects.filter(doctor = request.session['doctor']).count
    return render(request,'doctor/home.html',{'doctor':doctors,'count':noofpatient})

def master(request):
    doctors = Doctor.objects.get(id= request.session['doctor'])
    return render(request,'doctor/master.html',{'doctor':doctors})

def logout(request):
    del request.session['doctor']
    request.session.flush()
    return redirect( 'myhospital_app:home' )

def patients(request):
    return render(request,'doctor/patients.html')

def records(request):
    booking=Booking.objects.filter(doctor = request.session['doctor'],status='consulted')
    return render(request,'doctor/patient_records.html',{'booking':booking})

def appoinments(request):
    bookings = Booking.objects.filter(doctor = request.session['doctor'])
    
    return render(request,'doctor/appoinments.html',{'bookings':bookings})

 

def prescription(request ,booking_id):
    msg=''
    bookings = Booking.objects.get(id = booking_id)
    
    if request.method == 'POST':
        diagnosis = request.POST['diagnosis']
        medicine = request.POST['medicine']
        dosage = request.POST['dosage']
        frequency = request.POST['frequency']
        prescription = Prescription(
            diagnosis=diagnosis,
            medication_name=medicine,
            dosage=dosage,
            frequency=frequency,
            booking= bookings
        )
        prescription.status='consulted'
        
        prescription.save()
        bookings.status='consulted'
        bookings.save()
        msg='Prescription Added successfully'
        
        
    return render(request,'doctor/prescription.html',{'bookings':bookings,'msg':msg})




def discharge_req(request):
    return render(request,'doctor/discharge_request.html')

def patient_profile(request,bid):
    booking=Booking.objects.get(id=bid)
    print(booking)
    prescription = Prescription.objects.get(booking_id=booking)
    print("*************",prescription.id)
    return render(request,'doctor/patient_profile.html',{'booking':booking,'prescription':prescription})



def change_password(request):
    msg = ''
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if new_password == confirm_password:
            
            if len(new_password) >= 8:


                doctor = Doctor.objects.get(id= request.session['doctor'])

                if doctor.password == current_password:

                    Doctor.objects.filter(id= request.session['doctor']).update(password = confirm_password)
                    
                    msg = 'Password changed succesfully'
                else:
                    msg = 'Invalid password'
            else:
                msg = 'password should be min 8 characters'
        else:
            msg = 'password does not match'

    return render(request,'doctor/change_password.html',{'msg':msg})

 