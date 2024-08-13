from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import admins

urlpatterns = [
    path('',views.home,name='home'),
    path('journey',views.journey,name='journey'),
    path('contact',views.contact,name='contact'),
    path('login_user',views.login_user,name='login_user'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
    #adminurls
    path('admin_home',admins.admin_home,name='admin_home'),
    path('slider',admins.slider,name='slider'),
    path('intro',admins.intro,name='intro'),
    path('story_page',admins.story_page,name='story_page'),
    path('gallery',admins.gallery,name='gallery'),
    path('question_page',admins.question_page,name='question_page'),
    path('contact_page',admins.contact_page,name='contact_page'),
    path('edit_intro/<int:id>',admins.edit_intro,name='edit_intro'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
