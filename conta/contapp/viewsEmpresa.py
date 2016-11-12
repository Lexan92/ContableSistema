import os
import csv
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, time, timedelta
from contapp.models import  empresa, tipCuenta, rubCuenta, cuenta, partida, movimiento,impArchivo
from contapp.service import  ImpCatalago, errores, CatalogoCuentas,FormImportacion,FormEmpresa
from django.views.generic import ListView,CreateView
# Create your views here.
UPLOAD_FOLDER = '/var/www'

def Empresa(request):
    return render(request,'ErrorMigracion.html')

def loginRender(request):
    if request.session.has_key('codemp'):
        del request.session['codemp']
    if request.method == 'POST':
        # if request.session.has_key('codemp'):
        #     del request.session['codemp']
        emp = empresa.objects.get(codEmpresa = request.POST.get('codemp'))
        if emp:
            request.session['codemp'] = emp.codEmpresa
            # impp=CrearImportarArchivoView()
            return render(request, "areaT.html", {'logeado': True,'empresa': emp} )
        else:
            return render(request, "Home.html", {'mensaje': 'Error de inicio de sesión'})
    return render(request, "Home.html", {'mensaje': '','empresas':empresa.objects.all(),})
#UPLOAD_FOLDER = '/var/www/archivos'

def gestionEmpresa(request):
    # solo crea una nueva empresa y un catalogo por defecto que solo contendra los 6
    # tipos de cuentas
    if request.method == 'POST':
        form = FormEmpresa(request.POST)
        if form.is_valid():
            cd = form.cleaned_data#aqui extraigo solo la informacion del formulario
            emp=empresa()
            emp.nomEmpresa=cd['NOMBRE']
            emp.nit=cd['NIT']
            emp.nrc=cd['NRC']
            emp.save()
            cat=CatalogoCuentas(emp)
            cat.newCatalogo()
            return render(request, "Home.html", {'mensaje': '','empresas':empresa.objects.all()})
    else:
        form=FormEmpresa()
        return render(request, "Empresa/gestionEmpresa.html", {'form': form})