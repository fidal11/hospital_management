from django.shortcuts import render

# Create your views here.

def master(request):
    return render(request,'myhospital_app/master.html')
def login(request):
    return render(request,'myhospital_app/login.html')
def register(request):
    return render(request,'myhospital_app/register.html')
def home(request):
    return render(request,'myhospital_app/home.html')
def demo(request):
    return render(request,'myhospital_app/demo.html')
def patient_portal(request):
    return render(request,'myhospital_app/patient_portal.html')
def staff_login(request):
    return render(request,'myhospital_app/staff_login.html')
def doctor_login(request):
    return render(request,'myhospital_app/doctor_login.html')