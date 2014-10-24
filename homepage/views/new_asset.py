from django import forms
from django.conf import settings
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from django.http import HttpResponse, HttpResponseRedirect, Http404
from homepage import models as hmod


templater = MakoTemplateRenderer('homepage')


@view_function
def process_request(request):
    
    
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            
            f = hmod.Asset()
            f.currentlyActive = 'Yes'
            f.UID = form.cleaned_data['UID']
            f.organizationalTag = form.cleaned_data['organizationalTag']
            f.manufacturerPartNumber = form.cleaned_data['manufacturerPartNumber']
            f.description = form.cleaned_data['description']
            f.maintenanceNotes = form.cleaned_data['maintenanceNotes']
            
            loc = form.cleaned_data['location']
            location = hmod.Location.objects.get(UID=loc) 
            f.currentAssignedLocation = location
            #f.currentAssignedLocation = form.cleaned_data['currentAssignedLocation'] #MAKE THIS A LOCATION OBJECT
            
            man = form.cleaned_data['manufacturer']
            manufacturer = hmod.Manufacturer.objects.get(UID=man) 
            f.manufacturer = manufacturer
            #f.manufacturer = form.cleaned_data['manufacturer'] #MAKE THIS A MANUFACTURER OBJECTS

            f.save()
            
            
            return HttpResponseRedirect('/homepage/assets/')
    
    form = AssetForm()
    
    template_vars = { 'form': form, } 
    
    return templater.render_to_response(request, 'new_asset.html', template_vars, )
    
    
def getLocations():
    l = hmod.Location.objects.all()
    locationChoices = []
    count = 1
    tup1 = ()
    listy = list()
    for loc in l:
        tup1 = (loc.UID, str(str(loc.UID) + " " + str(loc.name)))
        listy.append(tup1)
        count += 1
    locationChoices = listy
    return locationChoices
    
def getManufacturers():
    m = hmod.Manufacturer.objects.all()
    manufacturerChoices = []
    count = 1
    tup1 = ()
    listy = list()
    for man in m:
        tup1 = (man.UID, str(str(man.UID) + " " + str(man.name)))
        listy.append(tup1)
        count += 1
    manufacturerChoices = listy
    return manufacturerChoices

class AssetForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(AssetForm, self).__init__(*args, **kwargs)
        self.fields['location'] = forms.ChoiceField(choices=getLocations(), required=True, label="Current Assigned Location",)
        self.fields['manufacturer'] = forms.ChoiceField(choices=getManufacturers(), required=True, label="Manufacturer",)
    
    UID = forms.CharField(required=True, label="Asset ID", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    organizationalTag = forms.CharField(required=True, label="Organizational Tag", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    manufacturerPartNumber = forms.CharField(required=True, label="Manufacturer Part Number", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    description = forms.CharField(required=True, label="Description", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    maintenanceNotes = forms.CharField(required=True, label="Maintenance Notes", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    #currentAssignedLocation = forms.CharField(required=True, label="Current Assigned Location (DD)", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    #manufacturer = forms.CharField(required=True, label="Manufacturer (DD)", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
 
