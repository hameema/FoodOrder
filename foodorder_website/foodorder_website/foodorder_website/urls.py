"""
Definition of urls for foodorder_website.
"""
from datetime import datetime
import pizza.views
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include , url
from django.contrib import admin
 
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'home', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url('admin/', admin.site.urls),
    url('',pizza.views.index,name="index"),

    # Uncomment the admin/doc line below to enable admin documentation:
    url('admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include('admin.site.urls')),
]
