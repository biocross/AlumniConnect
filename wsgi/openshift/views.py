from django.http import HttpResponse
from django.shortcuts import render_to_response
from openshift.models import *
from django.views.decorators.csrf import csrf_exempt

#Static pages
def home(request):
	return HttpResponse("Alumni Connect framework<br/><br/>Under Contruction as on 04/03/2013")

#Dynamic Pages / Forms / Pages which need arguments
def firstForm(request):
	myForm = UserForm()
	return render_to_response('firstRegistration.html' , {'firstRegistrationForm' : myForm.as_ul()  })
	
def profilePage(request):
	if request.method == "GET":
		userID = str(request.GET['id'])
		results = User.objects.filter(id=userID)
		userName = "did you enter a valid ID?"
		for x in results:
			userName = x
		if results:
			return render_to_response("profile.html", { 'user': x } )
		else:
			return HttpResponse("not found user")
			#Point to the standard 404 page




'''
@csrf_exempt
def EducationInsert(request):
	if request.method == "GET":
		myForm = EducationForm()
		return render_to_response('educationInsert.html', {'theForm': myForm.as_ul()})
	if request.method == "POST":
		form = EducationForm(request.POST)
		if (form.is_valid()):
			form.save()
			return HttpResponse("New education is now avalable!")
		else:
			return HttpResponse("nope there's a problem ;(")

'''

#Admin views:
@csrf_exempt
def BatchInsert(request):
	myForm = InsertBatch()
	if request.method == "GET":
		return render_to_response('generalInsertForm.html', {'theForm': myForm.as_ul()})
	if request.method == "POST":
		form = InsertBatch(request.POST)
		if (form.is_valid()):
			form.save()
			return render_to_response('generalInsertForm.html', {'theForm': myForm.as_ul() , 'status': "The option you provided has now been made available to users."  })
		else:
			return HttpResponse("nope there's a problem ;(")
@csrf_exempt
def BranchInsert(request):
	myForm = InsertBranch()
	if request.method == "GET":
		return render_to_response('generalInsertForm.html', {'theForm': myForm.as_ul()})
	if request.method == "POST":
		form = InsertBranch(request.POST)
		if (form.is_valid()):
			form.save()
			return render_to_response('generalInsertForm.html', {'theForm': myForm.as_ul() , 'status': "The option you provided has now been made available to users."  })
		else:
			return HttpResponse("nope there's a problem ;(")


#Data Acceptors
@csrf_exempt
def firstRegistrationSubmit(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if (form.is_valid()):
			form.save()
			return HttpResponse("inserted")
		else:
			return HttpResponse("error!")
		
	if request.method == "GET":
		return HttpResponse("GET used. nothing here, move along!")


#Temporary Views:
def AllUsers(request):
	results = User.objects.all()
	return render_to_response("allusers.html", { 'users': results  })
		





