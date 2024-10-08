from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
#authentication imports
from django.contrib.auth.models import Group
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_users,admin_only


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_home')
        else:
            messages.info(request,'username or password is incorrect') 

    return render(request,'auth/login.html')




def logoutUser(request):
    logout(request)
    return redirect('login_user')



#END AUTH
def home(request):
    slider = Slider.objects.all()
    titles = Slider.objects.all()
    introduction = Intro.objects.all()
    story = Story.objects.all()[:1]
    gall = Gallery.objects.all()
    questions = Question.objects.all()
    context = {
        'slider': slider,
        'titles':titles,
        'introduction':introduction,
        'story':story,
        'gall':gall,
        'questions':questions,
    }
    return render(request,'pages/client/home.html',context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,'contact info saved successfully')
        else:
            messages.error(request,'something went wrong')
        return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request,'pages/client/contact.html',context)



def journey(request):
    return render(request,'pages/client/journey.html')




