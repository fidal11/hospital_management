from django.urls import path
from .import views

 

app_name='myhospital_app'

urlpatterns =[
    path('master',views.master,name='master'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('home',views.home,name='home'),
    path('demo',views.demo,name='demo'),
    path('patient_portal',views.patient_portal,name='patient_portal'),
    path('staff_login',views.staff_login,name='staff_login'),
    path('doctor_login',views.doctor_login,name='doctor_login'),
    path('hospital/admin_login',views.admin,name='admin_login'),
    path('about_us',views.about_us,name='about_us'),
    path('contact',views.contact,name='contact'),
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    
    
    

]
      
