from django.db import models
from django import forms
from django.forms import ModelForm

#models



#Complex Models (Many to Many)
class Batch(models.Model):
	year = models.CharField(max_length="7")

	def __unicode__(self):
		return self.year

class Branch(models.Model):
	name = models.CharField(max_length="200")
	shortName = models.CharField(max_length="50")

	def __unicode__(self):
		return self.shortName



#Admin Forms
class InsertBatch(forms.ModelForm):
	class Meta:
		model = Batch

class InsertBranch(forms.ModelForm):
	class Meta:
		model = Branch




#Main Models
class User(models.Model):

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=40)
    #dob = models.DateField()
    batch = models.ManyToManyField(Batch)
    branch = models.ManyToManyField(Branch)
    email = models.EmailField()

    #education = models.ManyToManyField(Education)

    #headshot = models.ImageField(upload_to='/profilepictures')
    #added = models.DateTimeField(db_index=True, auto_now_add=True)
    #modified=models.DateTimeField(auto_now=True)





#Forms
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		


#Fundamentals
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
	
	

		
		
	


	
		
		
		