from django.shortcuts import render
from app.forms import *
from cliente.models import *
from tecnico.models import *

from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
# Create your views here.

def home(request):
    return render(request, 'app/template/base.html' )
def capacitate(request):
    return render(request, 'app/template/base.html' )
def registro(request):
	if request.method == 'POST':
		uf = Registrar(request.POST)
		up = UserProfileForm(request.POST, request.FILES)
		if uf.is_valid() and up.is_valid():
			uf.save()
			useradd = User.objects.get(username=uf.cleaned_data['username'])
			usuario = up.save(commit=False)
			usuario.user = useradd
			if 'foto' in request.FILES:
				usuario.foto = request.FILES['foto']
			usuario.save()

			return HttpResponseRedirect('/ingresar')
	else:
		uf = Registrar()
		up=UserProfileForm()
	return render(request, 'app/template/registrar.html', dict(userform=uf, userprofileform=up))
@login_required()	
def solicitar(request):
	return render(request, 'app/template/solicita.html' )
def tecnico(request):
	if request.method == 'POST':
		request.session['direccion'] = request.POST['Direccion']
		request.session['fecha'] = request.POST['Fecha'] + request.POST['Hora']
		request.session['dano'] = request.POST['dano']

		request.session['descripcion'] =request.POST['Marca']+ request.POST['Modelo']+ request.POST['descripcion']
		
		return render(request, 'app/template/tecnico.html' )
	else:
		return HttpResponseRedirect('/solicitar/')

def asignado(request):
		tecnico = Tecnico.objects.get(id=1)
		us= User.objects.get(username=request.user)
		cliente = Cliente.objects.get(user=us)
		direccion = request.session.get('direccion', False)
		fecha = request.session.get('fecha', False)
		dano = request.session.get('dano', False)
		descripcion = request.session.get('descripcion', False)
		Lon = 0
		Lat = 0
		cita = Cita(idCliente=cliente)
		cita.idTecnico = tecnico
		cita.direccion = direccion
		cita.fecha = fecha
		cita.dedescripcionDano = dano
		cita.descripcion = descripcion
		cita.save()
		return render(request, 'app/template/asignado.html')
