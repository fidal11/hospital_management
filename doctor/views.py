from django.shortcuts import render,redirect
from .models import Doctor
from django.db.models import F
from myhospital_app.models import Patient

# Create your views here.

def home(request):
    return render(request,'doctor/home.html')

def master(request):
    doctor = Doctor.objects.get(id= request.session['doctor'])
    return render(request,'doctor/master.html',{'doctor':doctor})

def logout(request):
    del request.session['doctor']
    request.session.flush()
    return redirect( 'myhospital_app:home' )

def patients(request):
    return render(request,'doctor/patients.html')

def records(request):
    patient=Patient.objects.filter(doctor = request.session['doctor'],status='consulted')
    return render(request,'doctor/patient_records.html',{'patient':patient})

def appoinments(request):
    patient = Patient.objects.filter(doctor = request.session['doctor'],status='pending')

    
    return render(request,'doctor/appoinments.html',{'patient':patient})

def prescription(request,aid):
    patient = Patient.objects.get(id=aid)
    msg=''
    if request.method=='POST':
        report = request.POST['report']
        medicine = request.POST['medicine']
       
        
        patient = Patient(
            report=report,
            medicine=medicine
        )
        patient.save()
    else:
        msg='error'
    
    return render(request,'doctor/prescription.html',{'patient':patient})

def discharge_req(request):
    return render(request,'doctor/discharge_request.html')

def consulted(request,pid):
    patient =Patient.objects.get(id=pid)
    patient.status='consulted'
    patient.save()
    return redirect('doctor:appoinments')



 