from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

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



#Django User (the superset of all users)
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    batch = models.ManyToManyField(Batch)
    branch = models.ManyToManyField(Branch)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

'''
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
'''




#Forms
class UserForm(forms.ModelForm):
	class Meta:
		model = User
		exclude = ("is_staff", "is_active", "is_superuser", "last_login", "date_joined" )
	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
		return user

class UserForm_Step2(forms.ModelForm):
	class Meta:
		model = UserProfile
		


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
	
	

		
		
	


	
		
		
		