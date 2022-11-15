from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.homePageView,name='home'),
    path('uregister/',views.userRegistrationView,name='uregistration'),
    path('insert/',views.insertUserDataBase,name='userinsert'),
    path('userloginpage/',views.userLoginPage,name='userloginpage'),
    path('ulogin/',views.uLogin,name='ulogin'),
]