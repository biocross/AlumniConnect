# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from messages.msg.models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def reg_form_alumni(request):
	if(request.method=='POST'):
		form = mod_form_user(request.POST)
		if(form.is_valid()):
			form.save()
			message = "Success!"
			form_t = mod_form_user()
			return render_to_response("reg_form_alumni.html",{'form':form_t,'msg':message})
	else :
		  form = mod_form_user()

	return render_to_response("reg_form_alumni.html",{'form':form})

@csrf_exempt
def send_message(request):
	if(request.method=='POST'):
		form = mod_form_msg(request.POST)
		if(form.is_valid()):
			form.save()
			message = "Success!"
			form_t = mod_form_msg()
			return render_to_response("send_message.html",{'form':form_t,'msg':message})
	else :
		  form = mod_form_msg()

	return render_to_response("send_message.html",{'form':form})
 

@csrf_exempt
def show_msg(request):
	if(request.method=='POST'):
		form = mod_getmsg(request.POST)
		if(form.is_valid()):
			u = form.cleaned_data['user_field'].id
			sent = Message.objects.filter(from_user = u)
			recvd = Message.objects.filter(to_user = u)
			form_t = mod_getmsg()
			return render_to_response("show_msg.html",{'form':form,'sent':sent,'recvd':recvd})
	else :
		  form = mod_getmsg()

	return render_to_response("show_msg.html",{'form':form})


@csrf_exempt
def login(request):
	if request.session['is_logged']:
		request.session['is_logged'] = True
	else:
		request.session['is_logged'] = False
	msg = ''
	if(request.method=='POST'):
		form = login_form(request.POST)
		if(form.is_valid() and not request.session['is_logged']):
			n = form.cleaned_data['name']
			r = form.cleaned_data['rollno']			
			usr = user.objects.filter(name=n,rollno=r)
			if usr:
				request.session['is_logged'] = True;
			else :
				msg = 'Error'
			return render_to_response("login.html",{'form':form,'msg':msg,'is_logged':request.session['is_logged']})
		else:
			msg = 'Error'
	else :
		  form = login_form()

	return render_to_response("login.html",{'form':form,'is_logged':request.session['is_logged']})