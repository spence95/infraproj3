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

    form = ManufacturerForm(initial={
        'UID': f.UID,
        'name': f.name,
        'address': f.address,
        'phone': f.phone,
    })
    
    

    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
                      
            f.UID = form.cleaned_data['UID']
            f.name = form.cleaned_data['name']
            f.address = form.cleaned_data['address']
            f.phone = form.cleaned_data['phone']
            
            f.save()
            return HttpResponseRedirect('/homepage/manufacturers/')
    
    template_vars = { 'form': form, } 
    
    return templater.render_to_response(request, 'edit_manufacturer.html', template_vars,)



  
class ManufacturerForm(forms.Form):
    
    UID = forms.CharField(required=True, label="Store ID", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    name = forms.CharField(required=True, label="Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    address = forms.CharField(required=True, label="Address", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    phone = forms.CharField(required=True, label="Phone", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))

    
    
    
    