from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Slider(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    sub_title = models.TextField()
    image = models.FileField(upload_to='images',blank=True,null=True)




class Intro(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    sub_title = models.TextField()
    image = models.FileField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.title


class Story(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    sub_title = models.TextField()
    image = models.FileField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
   user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
   image = models.FileField(upload_to='images',blank=True,null=True)
   date = models.DateField(auto_now=True)




class Question(models.Model):
   user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
   question = models.TextField()

   def __str__(self):
       return self.question
   
   
   
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name





