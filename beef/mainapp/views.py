from django.shortcuts import render,redirect



def home(request):
    return render(request,'pages/client/home.html')



def journey(request):
    return render(request,'pages/client/journey.html')


def contact(request):
    return render(request,'pages/client/contact.html')

