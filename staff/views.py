from django.shortcuts import render,redirect

# Create your views here.

def master(request):
    return render(request,'staff/master.html')

def home(request):
    return render(request,'staff/home.html')

def patients(request):
    return render(request,'staff/patients.html')

def appoinments(request):
    return render(request,'staff/appoinments.html')

def logout(request):
    del request.session['staff']
    request.session.flush()
    return redirect( 'myhospital_app:home' )