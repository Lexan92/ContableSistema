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


def estadosF(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""
            
    if emp:
        mensaj=""
        return render(request,'EstadosF/EstadoF.html',{'mensaje': mensaj,'empresa': emp})
    else:
        return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresa para iniciar','empresas':empresa.objects.all(),})    

def consultaEstadoF(request):
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

            if not request.POST.get('anio'):
                mensaj="Digite un año"
                return render(request,'EstadosF/EstadoF.html',{'mensaje': mensaj,'empresa': emp}) 
            else:
                anio=request.POST.get('anio')

            
            if request.POST.get('codTipo'):
                # if request.POST.get('codTipo')=="1":
                if request.POST.get('tipoEF')=="1":
                    tipo=request.POST.get('codTipo')                 
                    libro=libroMayor(emp,anio,mes,tipo)
                    estado="Balance General"
                    # se obtiene el balance general
                    estadoFinanciero=libro.getBlanceGeneral()                    
                    # tipos=libro.getTiposBlance()
                    # rubros=libro.getRubrosBlance()
                    mensaj=""
                    return render(request,'EstadosF/showEstadoF.html',{'mensaje': mensaj,
                    	'estadoF': estado,
                        'empresa': emp,
                    	'Estado': estadoFinanciero,                        
                        # 'rubEF': rubros,
                    	# 'tipos': tipos,
                    	'libro':libro})
                elif request.POST.get('tipoEF')=="2":
                    tipo=request.POST.get('codTipo')
                    libro=libroMayor(emp,anio,mes,tipo)
                    estado="Estado de Resultado"
                    # se obtiene el estado de resultado
                    estadoFinanciero=libro.getEstadoResultado()
                    # rubros=libro.getRubrosER()
                    # tipos=libro.getTiposER()
                    mensaj=""
                    return render(request,'EstadosF/showEstadoF.html',{'mensaje': mensaj,
                    	'estadoF': estado,
                    	'empresa': emp,
                        # 'rubEF': rubros,
                    	'tipos': tipos,
                    	'libro':libro})
            else:
            	mensaj="selecione un tipo de Estado Financiero"
            	return render(request,'EstadosF/EstadoF.html',{'mensaje': mensaj,'empresa': emp})       
        elif request.session.has_key('codemp') == False: #Usuario no ha iniciado sesión
            return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresar para iniciar','empresas':empresa.objects.all(),})
            # confirma si  existe una sesioncon una empresa
    elif emp:
        return render(request,'areaT.html',{'empresa': emp})
    else:
        return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresa para iniciar','empresas':empresa.objects.all(),})    