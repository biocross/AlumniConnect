from django.db import models
from django import forms
from django.forms import ModelForm

#models
class User(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    #dob = models.DateField()
    batch = models.IntegerField(max_length=4)
    branch = models.CharField(max_length=30)
    email = models.EmailField()
    #headshot = models.ImageField(upload_to='/profilepictures')
    #added = models.DateTimeField(db_index=True, auto_now_add=True)
    #modified=models.DateTimeField(auto_now=True)

#forms
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		


#fundamentals
class OpenPrivacy(models.Model):
	UserID1 = models.ForeignKey(User, related_name = "Request_from_user")
	UserID2 = models.ForeignKey(User, related_name = "Request_to_user")
	requestStatus = models.BooleanField()
	'''
	requestStatus:
		if true: means accepted
		if false: means waiting
		if a model like this does not exist : that means no request has been sent yet.
	'''
	
	

		
		
	


	
		
		
		