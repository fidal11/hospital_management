from django.urls import path
from .import views

app_name='staff'

urlpatterns =[
    path('master',views.master,name='master'),
    path('home',views.home,name='home'),
    path('patients',views.patients,name='patients'),
    path('appoinments',views.appoinments,name='appoinments'),
    path('logout',views.logout,name='logout'),
    
    
    
    
    
]