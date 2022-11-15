from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import UserDatabase
from .serializers import *
from rest_framework.renderers import JSONRenderer

# Create your views here.
def homePageView(request):
    return render(request, 'home.html')

def userRegistrationView(request):
    return render(request, 'uregistration.html')

def insertUserDataBase(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        #First we check user is already exist or not
        user=UserDatabase.objects.filter(Email=email)
        if user:
            msg= "This Email is already exist"
            return render(request,'uregistration.html',{'msg':msg})
        else:
            if password == cpassword:
                newuser = UserDatabase.objects.create(Firstname=fname,Lastname=lname,Email=email
                                    ,Contact=contact,Password=password)
                msg = "User register Successfully"
                return render(request,'home.html',{'msg':msg})
            else:
                msg = "Password and Confirm Password Doesnot Match"
                return render(request,"uregistration.html",{'msg':msg})

def userLoginPage(request):
    return render(request,'ulogin.html')

def uLogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=UserDatabase.objects.get(Email=email)
        if user:
            if user.Password==password:
                request.session['Firstname']=user.Firstname
                request.session['Lastname']=user.Lastname
                request.session['Email']=user.Email
                return render(request,'userdashboard.html')
        else:
            msg="Invalid Email or Password"
            return render(request,'ulogin.html',{'msg':msg})
    else:
        msg="user dose not exit"
        return render(request,'uregistration.html',{'msg':msg})


def user_details_pk(request,pk=None):
    user=UserDatabase.objects.get(id=pk)
    serializer=UserDatabaseSerializer(user)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    #return JsonResponse(serializer.data)

def user_details_list(request):
    user=UserDatabase.objects.all()
    serializer=UserDatabaseSerializer(user,many=True)
    #json_data= JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

