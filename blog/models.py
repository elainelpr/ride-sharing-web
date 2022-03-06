from django.db import models
from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.

class CreatedUsersForm(UserCreationForm):
   email = forms.EmailField(error_messages={'required':'email should not be empty'})

   class Meta:
      model = User
      fields = ['username', 'password1', 'password2', 'email']

class Driver(models.Model):

   driver_name = models.CharField(max_length=32)
   vehicle_type = models.CharField(max_length=32)
   license_num = models.CharField(max_length=32)
   max_numPass = models.IntegerField(default=0)
   username = models.CharField(max_length=32)
   email = models.CharField(max_length=32)

   #class Meta:
   #   db_table = "blog_users"  #指定表名
   #可以不用指定表名，默认表名是当前app名_类名


class Sharer(models.Model):
   user_id = models.IntegerField()
   sharer_numPass = models.IntegerField(default=0)

#每一个class类对应一个表
#Model类已经包含了增删改查的功能
class RideRequests(models.Model):  #该user继承了django中的db里面的Models类
   start=models.CharField(max_length=32)  #每一个属性代表一个字段，每一个字段代表定义的类型. char 代表字符串类型（告诉数据表，name是char类型）
   dest=models.CharField(max_length=32)
   numPass= models.IntegerField(default=20) 
   isShare=models.BooleanField()
   addDate=models.DateField()
   addTime=models.TimeField()
   status=models.IntegerField(default=0)
   user = models.ForeignKey(User,related_name='ride_owner', on_delete=models.CASCADE)
   driver = models.ForeignKey(Driver,related_name='ride_driver', on_delete=models.CASCADE, null=True)
   sharer = models.ForeignKey(Sharer, related_name='ride_sharer', on_delete=models.CASCADE)
   

   def printDate(self):
      return str(self.addDate)
   
   def printTime(self):
      return str(self.addTime)


