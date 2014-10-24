from django import forms
from django.conf import settings
from django_mako_plus.controller.router import MakoTemplateRenderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django_mako_plus.controller import view_function
from homepage import models as hmod

templater = MakoTemplateRenderer('homepage')

@view_function
def process_request(request):
    
    
    f = hmod.Manufacturer.objects.get(UID=request.urlparams[0])
    f.delete()
    return HttpResponseRedirect('/homepage/manufacturers/')


