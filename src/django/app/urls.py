"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app.views import *
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('',login_required(VotarView.as_view()),name='votar-main'),
    url(r'^common/', include('common.urls')),
    #path('',login_required(ResultadosView.as_view()),name='resultados-list'),
]
