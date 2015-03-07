from django.conf.urls import url
from django.contrib import admin
from cliente import views

urlpatterns = (
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
	url(r'^registrar/', 'app.views.registro', name='registro'),
    )