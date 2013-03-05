from django.conf.urls import patterns, include, url
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'openshift.views.home'),
     url(r'^firstRegistration$', 'openshift.views.Registration'),   #first registration
     url(r'^firstRegistrationSubmit$', 'openshift.views.firstRegistrationSubmit'), #submit first reg
     url(r'^registrationStep2$', 'openshift.views.Registration_Step2'), #second registation step
     url(r'^UserRegComplete$', 'openshift.views.UserRegComplete'), #second step complete

     url(r'^home$', 'openshift.views.Home'),    #Home page - Dashboard
     url(r'^login$', 'openshift.views.Login'),
     url(r'^logout$', 'openshift.views.Logout'),  
     




     #Admin URLS:
     url(r'^insertBatch', 'openshift.views.BatchInsert'),
     url(r'^insertBranch', 'openshift.views.BranchInsert'),


	 url(r'^profile$', 'openshift.views.profilePage'),



    # url(r'^AlumniConnect/', include('AlumniConnect.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

     url(r'^allusers$', 'openshift.views.AllUsers'),
     url(r'^admin/', include(admin.site.urls)),
)
