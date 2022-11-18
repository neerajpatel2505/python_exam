from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.homePageView,name='home'),
    path('uregister/',views.employeeRegistrationView,name='eregistration'),
    path('insert/',views.insertemployeeDataBase,name='employeeinsert'),
    path('employeeloginpage/',views.employeeLoginPage,name='employeeloginpage'),
    path('elogin/',views.eLogin,name='elogin'),
    
    path('employee_data/<int:pk>/',views.employee_details_pk,name='employee_data'),
    path('employee_list/',views.employee_details_list,name='employee_data'),
    
]