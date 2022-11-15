from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.homePageView,name='home'),
    path('uregister/',views.userRegistrationView,name='uregistration'),
    path('insert/',views.insertUserDataBase,name='userinsert'),
    path('userloginpage/',views.userLoginPage,name='userloginpage'),
    path('ulogin/',views.uLogin,name='ulogin'),
    
    path('user_data/<int:pk>/',views.user_details_pk,name='user_data'),
    path('user_list/',views.user_details_list,name='user_data'),
    
]