from django.urls import path
from .import views

app_name='doctor'

urlpatterns =[
    path('home',views.home,name='home'),
    path('master',views.master,name='master'),
    path('logout',views.logout,name='logout'),
    path('patients',views.patients,name='patients'),
    path('patient/records',views.records,name='records'),
    path('appoinments',views.appoinments,name='appoinments'),
    path('prescription/<int:booking_id>',views.prescription,name='prescription'),
    path('discharge/request',views.discharge_req,name='discharge_request'),
    path('patient/profile/<int:bid>',views.patient_profile,name='patient_profile'),
    path('change/password',views.change_password,name='change_password'),
    
     
    
    
        
    
    
    
    
]