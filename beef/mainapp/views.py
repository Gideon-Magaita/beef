from django.shortcuts import render,redirect
from .models import *


def home(request):
    slider = Slider.objects.all()
    titles = Slider.objects.all()[:1]
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





def journey(request):
    return render(request,'pages/client/journey.html')


def contact(request):
    return render(request,'pages/client/contact.html')

