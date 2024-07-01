from django import forms
from django.forms import ModelForm
from .models import *


class SliderForm(ModelForm):      
    class Meta:
        model = Slider
        fields = ['image','title','sub_title']
        
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'sub_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter sub-title'}),
        }


class IntroForm(ModelForm):      
    class Meta:
        model = Intro
        fields = ['image','title','sub_title']
        
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control','required':'required'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title','required':'required', 'placeholder': 'Enter title'}),
            'sub_title': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter sub-title','required':'required', 'placeholder': 'Enter sub-title'}),
        }


class StoryForm(ModelForm):      
    class Meta:
        model = Story
        fields = ['image','title','sub_title']
        
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control','required':'required'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title','required':'required', 'placeholder': 'Enter title'}),
            'sub_title': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter sub-title','required':'required', 'placeholder': 'Enter sub-title'}),
        }



class GalleryForm(ModelForm):      
    class Meta:
        model = Gallery
        fields = ['image']
        
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control','required':'required'}),
        }


class QuestionForm(ModelForm):      
    class Meta:
        model = Question
        fields = ['question']
        
        widgets = {
            'question': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter sub-title','required':'required', 'placeholder': 'Enter sub-title'}),
        }