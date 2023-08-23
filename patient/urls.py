from django.urls import path
from .import views
 

app_name='patient'

urlpatterns =[
    path('master',views.master,name='master'),
    ]