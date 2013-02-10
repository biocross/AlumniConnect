from django.http import HttpResponse
from django.shortcuts import render_to_response
from openshift.models import UserForm, User
from django.views.decorators.csrf import csrf_exempt

#Static pages
def home(request):
	return HttpResponse("Alumni Connect framework\n\nUnder Contruction as on 04/02/2013")

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
			return render_to_response("profile.html", )
		else:
			return HttpResponse("not found user")
			#Point to the standard 404 page








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
		





