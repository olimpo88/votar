#encoding:utf-8
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import HttpResponseRedirect


# Logger
import logging
logger = logging.getLogger('django')


class VotarView(TemplateView):
	template_name = 'votar/main.html'







#@login_required
#def main(request):
#		return render_to_response('no_es_empleado.html')
