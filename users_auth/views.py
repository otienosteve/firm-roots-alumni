from django.shortcuts import render

# Create your views here.

def login(request):

    return render(request,"login.html")


def register(request):

    if request.method=='POST':
        print("posted")

    return render(request,"register.html")


