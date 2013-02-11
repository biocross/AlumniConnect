from django.conf.urls import *
from messages.msg.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r"^reg/$",reg_form_alumni),
	(r'^reg/redirect_reg/$',reg_form_alumni),
	(r'^send_message/$',send_message),
    (r'^show_msg/$',show_msg),
    (r'^login/$',login),
    # Examples:
    # url(r'^$', 'messages.views.home', name='home'),
    # url(r'^messages/', include('messages.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
