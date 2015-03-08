from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from cliente import views

urlpatterns = (
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
	url(r'^registrar/', 'app.views.registro', name='registro'),
	url(r'^ingresar/', login, {'template_name': 'app/template/ingresar.html', }, name="ingresar"),
	url(r'^solicitar/', 'app.views.solicitar', name='solicitar'),
	url(r'^capacitate/', 'app.views.capacitate', name='capacitate'),
	url(r'^tecnico/', 'app.views.tecnico', name='tecnico'),
	url(r'^asignado/', 'app.views.asignado', name='asignado'),
 	url(r'^salir/', logout, {'template_name': 'app/template/base.html', }, name="salir"),


    )