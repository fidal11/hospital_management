from django.urls import path
from .import views

app_name=' admin_app'

urlpatterns =[
    path('admin_dash',views.admin_dash,name='admin_dash'),
    path('admin_doctor',views.admin_doctor,name='admin_doctor'),
]