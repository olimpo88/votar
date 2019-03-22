from django.urls import path
from vote.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(VotarView.as_view()),name='votar-main'),
	path('main/',login_required(VotarView.as_view()),name='votar-main'),
	path('question/',login_required(PreguntaView.as_view()),name='question'),
	path('users/',login_required(UserView.as_view()),name='users'),
	path('users/<slug:buscar>',login_required(UserView.as_view()),name='users'),
	path('add_user/<int:id_user>',login_required(AddUserView.as_view()),name='add-users'),
	path('set_user',login_required(SetUserView.as_view()),name='set-users'),
]