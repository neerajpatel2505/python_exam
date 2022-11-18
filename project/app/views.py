from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import EmployeeDatabase
from .serializers import *
from rest_framework.renderers import JSONRenderer

# Create your views here.
def homePageView(request):
    return render(request, 'home.html')

def employeeRegistrationView(request):
    return render(request, 'eregistration.html')

def insertemployeeDataBase(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        #First we check user is already exist or not
        user=EmployeeDatabase.objects.filter(Email=email)
        if user:
            msg= "This Email is already exist"
            return render(request,'eregistration.html',{'msg':msg})
        else:
            if password == cpassword:
                newuser = EmployeeDatabase.objects.create(Firstname=fname,Lastname=lname,Email=email
                                    ,Contact=contact,Password=password)
                msg = "User register Successfully"
                return render(request,'home.html',{'msg':msg})
            else:
                msg = "Password and Confirm Password Doesnot Match"
                return render(request,"eregistration.html",{'msg':msg})

def employeeLoginPage(request):
    return render(request,'elogin.html')

def eLogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=EmployeeDatabase.objects.get(Email=email)
        if user:
            if user.Password==password:
                request.session['Firstname']=user.Firstname
                request.session['Lastname']=user.Lastname
                request.session['Email']=user.Email
                return render(request,'employeedashboard.html')
        else:
            msg="Invalid Email or Password"
            return render(request,'elogin.html',{'msg':msg})
    else:
        msg="user dose not exit"
        return render(request,'eregistration.html',{'msg':msg})


def employee_details_pk(request,pk=None):
    user=EmployeeDatabase.objects.get(id=pk)
    python_data=EmployeeDatabaseSerializer(user)
    json_data= JSONRenderer().render(python_data.data)
    return HttpResponse(json_data,content_type='application/json')
    #return JsonResponse(python_data.data)

def employee_details_list(request):
    user=EmployeeDatabase.objects.all()
    python_data=EmployeeDatabaseSerializer(user,many=True)
    #json_data= JSONRenderer().render(python_data.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(python_data.data,safe=False)

