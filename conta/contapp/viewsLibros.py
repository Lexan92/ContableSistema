import os
import csv
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, time, timedelta
from contapp.models import  empresa, tipCuenta, rubCuenta, cuenta, partida, movimiento,impArchivo
from contapp.service import  *
from django.views.generic import ListView,CreateView
# Create your views here.
UPLOAD_FOLDER = '/var/www'


def Libros(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""
            
    if emp:
        mensaj=""
        return render(request,'Libros/Libros.html',{'mensaje': mensaj,'empresa': emp})
    else:
        return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresa para iniciar','empresas':empresa.objects.all(),})    

def consultaLibro(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""
        # si el metodo no es es post esntonces sele mostrara el fomulario de creacion de cuenta
    if request.method == 'POST':
        # si el metodo es post entonces ya fueron confirmados los datos de la cuenta crear y 
        if request.session.has_key('codemp'):
            if request.POST.get('mes'):
                mes=request.POST.get('mes')
            else:
                mes=""
            anio=request.POST.get('anio')
            if request.POST.get('codlibro'):
                if request.POST.get('codlibro')=="1":
                    tipo=request.POST.get('codlibro')                 
                    libro=libroMayor(emp,anio,mes,tipo)
                    mensaj=""
                    return render(request,'Libros/showLibro.html',{'mensaje': mensaj,'empresa': emp,'libro':libro})
                elif request.POST.get('codlibro')=="2":
                    tipo=request.POST.get('codlibro')
                    libro=libroMayor(emp,anio,mes,tipo)
                    mensaj=""
                    return render(request,'Libros/showLibro.html',{'mensaje': mensaj,'empresa': emp,'libro':libro})
            else:
            	mensaj="selecione un tipo de libro "
            	return render(request,'Libros/Libros.html',{'mensaje': mensaj,'empresa': emp})       
        elif request.session.has_key('codemp') == False: #Usuario no ha iniciado sesión
            return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresar para iniciar','empresas':empresa.objects.all(),})
            # confirma si  existe una sesioncon una empresa
    elif emp:
        return render(request,'areaT.html',{'empresa': emp})
    else:
        return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresa para iniciar','empresas':empresa.objects.all(),})    