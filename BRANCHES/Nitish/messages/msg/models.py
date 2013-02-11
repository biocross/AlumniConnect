from django.db import models
from django import forms
from django.forms import ModelForm



class user(models.Model):
	name = models.CharField(max_length=30)
	rollno = models.IntegerField(max_length = 20)
	def __unicode__(self):
		return self.name


# Create your models here.
class Message(models.Model):
	from_user = models.ForeignKey(user,related_name="Message_from_user")
	to_user = models.ForeignKey(user,related_name="Message_to_user")
	content = models.TextField(max_length=1000)
	def get_from_name(self):
		return self.from_user.name
	def get_to_name(self):
		return self.to_user.name
	
class req_user(models.Model):
    user_field = models.ForeignKey(user) 

class mod_form_user(forms.ModelForm):
	class Meta:
		model = user

class mod_form_msg(forms.ModelForm):
	class Meta:
		model = Message


class mod_getmsg(forms.ModelForm):
	class Meta:
		model = req_user

class login_form(forms.Form):
	name = forms.CharField()
	rollno = forms.IntegerField()		

