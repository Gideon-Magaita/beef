from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages



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




