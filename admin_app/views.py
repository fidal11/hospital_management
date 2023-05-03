from django.shortcuts import render

# Create your views here.

def admin_dash(request):
    return render(request,'admin_app/admin_dash.html')
def admin_doctor(request):
    return render(request,'admin_app/admin_doctor.html')
