from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import admins

urlpatterns = [
    path('',views.home,name='home'),
    path('journey',views.journey,name='journey'),
    path('contact',views.contact,name='contact'),
    #adminurls
    path('admin_home',admins.admin_home,name='admin_home'),
    path('slider',admins.slider,name='slider'),
    path('intro',admins.intro,name='intro'),
    path('story_page',admins.story_page,name='story_page'),
    path('gallery',admins.gallery,name='gallery'),
    path('question_page',admins.question_page,name='question_page'),
    path('contact_page',admins.contact_page,name='contact_page'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
