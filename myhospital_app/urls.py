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

]
      
