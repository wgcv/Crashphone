from django.shortcuts import render
from app.forms import *
from cliente.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def home(request):
    now = 32
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

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

			return HttpResponseRedirect('/')
	else:
		uf = Registrar()
		up=UserProfileForm()
	return render(request, 'app/template/registrar.html', dict(userform=uf, userprofileform=up))