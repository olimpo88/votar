#encoding:utf-8
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from app.helpers.paginator import PaginatorHelper
from django.db.models import Q
from accounts.models import Activity_log


# Logger
import logging
logger = logging.getLogger('django')


class VotarView(TemplateView):
	template_name = 'vote/main.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		admin = False
		if self.request.user.is_superuser:
			admin=True
		context['admin'] = admin
		return context


class PreguntaView(TemplateView):
	template_name = 'vote/question.html'


class UserView(TemplateView):
	template_name = 'vote/users.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		#print buscar
		users=User.objects.all().order_by('username')
		if 'buscar' in self.kwargs.keys():
			buscar=self.kwargs['buscar']
			users=users.filter( Q(first_name__icontains=buscar) | Q(last_name__icontains=buscar) | Q(username__icontains=buscar) )
		else:
			buscar=''
		listado = PaginatorHelper(users, 15);
		page = 1;
		if 'page' in self.request.GET.keys():
			page = self.request.GET['page']
		context['list_users'] = listado.getPage(page)
		return context


class AddUserView(TemplateView):
	template_name = 'vote/add_user.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user=None
		if 'id_user' in self.kwargs.keys():
			try:
				user=User.objects.get(id=self.kwargs['id_user'])
				print (user)
			except OstUserEmail.DoesNotExist:
				print ("DoesNotExist")
		context['user'] = user
		return context

#@login_required
#def main(request):
#		return render_to_response('no_es_empleado.html')

class SetUserView(View):

	def post(self,request,*args,**kwargs):

		myjson = {
			'error': "",
			'success': False,
		}
		print (request.POST)
		if "username" in request.POST.keys():
			username=request.POST['username']
			name=request.POST['name']
			last_name=request.POST['last_name']
			email=request.POST['email']
			password=request.POST['password']
			is_admin=request.POST['is_admin']

			if is_admin=="1":
				is_admin=True
			else:
				is_admin=False


			try:
				user_exist= User.objects.get(username=username)
				myjson['error']= "username exist"
				return HttpResponse(json.dumps(myjson))
			except User.DoesNotExist:
				user = User.objects.create_user(username=username,
		                                 		email=email,
		                                 		password=password)
				if password:
					#user.password=password
					user.set_password(password)
				user.first_name=name
				user.last_name=last_name
				user.is_superuser=is_admin
				user.save()
				myjson['success']= True
			Activity_log(action='EDIT USER', xforward="", user_affected=request.user, result="Edit User --> name: %s"%user).save()


		elif "id_user" in request.POST.keys():
			name=request.POST['name']
			last_name=request.POST['last_name']
			email=request.POST['email']
			password=request.POST['password']
			is_admin=request.POST['is_admin']		
			user= User.objects.get(id=request.POST['id_user'])
			if is_admin=="1":
				is_admin=True
			else:
				is_admin=False
			user.first_name=name
			user.last_name=last_name
			user.is_superuser=is_admin
			user.email=email
			if password:
				#user.password=password
				print (password)
				user.set_password(password)
			user.save()
			myjson['success']= True
			Activity_log(action='SET USER', xforward="", user_affected=request.user, result="Add User --> name: %s"%user).save()
		else:
			myjson['error']= "No se pasaron los datos por post"

		return JsonResponse(myjson)