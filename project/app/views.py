from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # return render(request,'home.html')
    return HttpResponse("Welcome to home page")