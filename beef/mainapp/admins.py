from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.http import JsonResponse
#authentication imports
# from django.contrib.auth.models import Group
# from django.contrib.auth.forms  import UserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from .decorators import unauthenticated_user,allowed_users,admin_only



# @login_required(login_url='login_user')
# @allowed_users(allowed_roles=['admins'])
def admin_home(request):
    return render(request, 'pages/admins/home.html')


def slider(request):
    slider = Slider.objects.all()
    if request.method == 'POST':
        form = SliderForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'slider saved successfully')
            return redirect('slider')
        else:
            messages.error(request,'something went wrong')
            return redirect('slider')
    else:
        form = SliderForm()
    context={
        'form': form,
        'slider': slider,
    }
    return render(request, 'pages/admins/sliders.html',context)



def intro(request):
    introduction = Intro.objects.all()
    if request.method == 'POST':
        form = IntroForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'details saved successfully')
            return redirect('intro')
        else:
            messages.error(request,'something went wrong')
            return redirect('intro')
    else:
        form = IntroForm()
    context={
        'form': form,
        'introduction':introduction,
    }
    return render(request, 'pages/admins/intro.html',context)



def story_page(request):
    story = Story.objects.all()
    if request.method == 'POST':
        form = StoryForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'details saved successfully')
            return redirect('story_page')
        else:
            messages.error(request,'something went wrong')
            return redirect('story_page')
    else:
        form = IntroForm()
    context={
        'form': form,
        'story':story,
    }
    return render(request, 'pages/admins/story.html',context)


def gallery(request):
    gall = Gallery.objects.all()
    if request.method == 'POST':
        form = GalleryForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'details saved successfully')
            return redirect('gallery')
        else:
            messages.error(request,'something went wrong')
            return redirect('gallery')
    else:
        form = GalleryForm()
    context={
        'form': form,
        'gall':gall,
    }
    return render(request, 'pages/admins/gallery.html',context)


def question_page(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        form = QuestionForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'details saved successfully')
            return redirect('question_page')
        else:
            messages.error(request,'something went wrong')
            return redirect('question_page')
    else:
        form = QuestionForm()
    context={
        'form': form,
        'questions':questions,
    }
    return render(request, 'pages/admins/question.html',context)

