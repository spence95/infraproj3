from django.conf import settings
from django_mako_plus.controller.router import MakoTemplateRenderer
from django_mako_plus.controller import view_function
from homepage import models as hmod


templater = MakoTemplateRenderer('homepage')

@view_function
def process_request(request):
  template_vars = {
    'wilson': "AWESOME",
    'manufacturers': hmod.Manufacturer.objects.all().order_by('UID')
  }
  return templater.render_to_response(request, 'manufacturers.html', template_vars)