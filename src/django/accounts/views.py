#encoding:utf-8
from django.contrib.auth import authenticate, login as djlogin, logout as djlogout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template  import RequestContext
import json
from accounts.models import Activity_log
from datetime import datetime, timedelta
import base64


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def dologin(request):
	myjson = {
		'errors': {},
		'message': '',
		'success': False,
		'redirect': '',
		'sync': ''
	}
	username=request.POST['username']
	if request.session.test_cookie_worked():
		cant_fails=Activity_log.objects.filter(action='DOLOGIN', user_affected=username, date__gt=(datetime.now()-timedelta(minutes=10)), result__startswith='False').count()
		if cant_fails>=5:
			myjson['errors']['reason']=u'Ha superado la cantidad máxima de intentos.'
		else:
			user = authenticate(username=username,
					password=request.POST['password'])
			if user is not None:
				if user.is_active:
					request.session.delete_test_cookie()
					djlogin(request, user)
					myjson['success'] = True
					myjson['message'] = 'Bienvenido, %s!' % (user.get_full_name(),)
					myjson['redirect'] = '/'
					myjson['errors']['reason'] = 'Login correcto.'
				else:
					myjson['errors']['reason'] = 'Cuenta deshabilitada.'
			else:
				myjson['errors']['reason'] = 'Usuario y/o clave invalida.'
	else:
		myjson['errors']['reason'] = 'Por favor, habilite las Cookies en su navegador.'
	Activity_log(action='DOLOGIN', xforward=get_client_ip(request), user_affected=username, result="%s - %s"%(myjson['success'], myjson['errors']['reason'])).save()

	return HttpResponse(json.dumps(myjson))


def login(request):
	request.session.set_test_cookie()
	return render(request,"login.html")

def permission_denied(request):
	return render(request,"permission_denied.html")

@login_required
def logout(request, next_page = '/accounts/login/'):
	djlogout(request)
	return HttpResponseRedirect(next_page)

def sin_permiso(request):
	return render_to_response("sin_permiso.html")