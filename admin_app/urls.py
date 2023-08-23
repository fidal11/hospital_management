from django.urls import path
from .import views

app_name= 'admin_app'

urlpatterns =[
    path('admin_master',views.admin_master,name='admin_master'),
    path('admin_doctor',views.admin_doctor,name='admin_doctor'),
    path('add_doctor',views.add_doctor,name='add_doctor'),
    path('home',views.home,name='home'),
    path('staffs',views.staffs,name='staffs'),
    path('staff/register',views.staff_reg,name='staff_register'),
    path('logout',views.logout,name='logout'),
    path('doctor/records',views.doc_records,name='doc_records'),
    path('staff/records',views.staff_rec,name='staff_rec'),
    path('departments',views.departments,name='departments'),
    path('appoinments',views.appoinments,name='appoinments'),
    
     
    
    
    
    
    
    
]