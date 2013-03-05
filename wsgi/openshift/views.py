from django.http import *
from django.shortcuts import render_to_response
from openshift.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import *

#Static pages
def home(request):
	return HttpResponse("Alumni Connect framework<br/><br/>Under Contruction as on 04/03/2013")

#Dynamic Pages / Forms / Pages which need arguments
def Registration(request):
	myForm = UserForm()
	return render_to_response('firstRegistration.html' , {'firstRegistrationForm' : myForm.as_p()  })

@login_required(login_url='/login')
def Registration_Step2(request):
	myForm = UserForm_Step2()
	if(request.user.is_authenticated()):
		logoutButton = "<button "
		session = "you are logged in as " + request.user.username
		return render_to_response('registrationStep2.html', { 'secondForm' : myForm.as_ul(), 'session' : session   }  )
	else:
		session = "you're not logged in .. wtf?"
		return HttpResponse("<h3>Sorry, you cant access this page without logging in.</h3>")
	
@csrf_exempt
def Login(request):
	if request.method =="GET":
		if (request.user.is_authenticated()):
			return HttpResponseRedirect("/home")
		else:
			return render_to_response("login.html")

	if request.method =="POST":
		username = request.POST['username']
    	password = request.POST['password']
    	user = authenticate(username=username, password=password)
    	if user is not None:
        	if user.is_active:
        		login(request, user)
        		# Redirect to a success page.
        		return HttpResponseRedirect("/home")
        	else:
        		return render_to_response("login.html", {'message' : "Sorry, your credentials are invalid."})
        else:
        	return render_to_response("login.html", {'message' : "Sorry, your credentials are invalid."})


def Logout(request):
	if (request.user.is_authenticated()):
		logout(request)
		return render_to_response("login.html", {'message': "You have successfully logged out." })
	else:
		return render_to_response("login.html", {'message': "You need to login first to logout!" })

@csrf_exempt
def firstRegistrationSubmit(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if (form.is_valid()):
			form.save()
			new_user = authenticate(username=request.POST['username'], password=request.POST['password'])
			login(request, new_user)
			UserProfile.objects.create(user=request.user)
			return HttpResponseRedirect("/registrationStep2")
		else:
			return HttpResponse("error!")
		
	if request.method == "GET":
		return HttpResponse("GET used. nothing here, move along!")

@csrf_exempt
def UserRegComplete(request):
	if request.method == "POST":
		form = UserForm_Step2(request.POST)
		if (form.is_valid()):
			form.save()
			return HttpResponseRedirect("/home")
		else:
			return HttpResponse(form.errors)


@login_required(login_url="/login")
def Home(request):
	user = request.user
	profile = user.get_profile()
	return render_to_response("home.html", {'user' : user, "profile": profile } )

	
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




#Temporary Views:
def AllUsers(request):
	results = User.objects.all()
	return render_to_response("allusers.html", { 'users': results  })
		





