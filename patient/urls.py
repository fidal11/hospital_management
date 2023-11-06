from django.urls import path
from .import views
 

app_name='patient'

urlpatterns =[
    path('master',views.master,name='master'),
    path('home',views.home,name='home'),
    path('appoinments',views.appoinments,name='appoinments'),
    path('logout',views.logout,name='logout'),
    path('new/booking',views.new_booking,name='new_booking'),
    path('appoinment/list',views.appoinment_list,name='appoinment_list'),
    path('change/password',views.change_password,name='change_password'),
    path('prescriptions',views.prescriptions,name='prescriptions'),
    path('view/prescriptions/<int:bid>',views.view_prescription,name='view_prescriptions'),
    
    
    
    
    ]