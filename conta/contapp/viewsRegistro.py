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


def Registro(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""
    if emp:
        return render(request,'Registros/Registro.html',{'empresa': emp})

def consultaPartida(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""
    partidas=partida.objects.filter(codEmpresa=emp.codEmpresa) 
    if partidas:
               
        return render(request,'Registros/msgPartida.html',{'msg': 'registros','partidas': partidas})
                # return render(request,'Registros/msgPartida.html',{'msg': 'ya casi man','partidas': partidas})
                # return render(request,'msgPartida.html',{'msg': 'ya casi man','cod': a,'debe': b,'haber': c,'long': d,'partidas': partidas})
    else:
        return render(request,'Registros/msgPartida.html',{'msg': 'no hay registros'}) 



def regPartida(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception:
        emp=""
    if emp:
        if request.method == 'POST':
            # contiene los codigos de las cuentas a ingresar
            a=request.POST.getlist('cod')
            # contiene los valores de debe para cada cuenta
            b=request.POST.getlist('debe')
            # contiene los valores de haber para cada cuenta
            c=request.POST.getlist('haber')
           
            d=len(a)
            formato = "%Y-%m-%d"                  
            ok=True            

            # fecha=request.POST.get('fechaP')
            numPartida=request.POST.get('numeroP')
            # comienza registro de partida
            try:
                partid=partida()
                if request.POST.get('fechaP'):
                    fecha = datetime.strptime(request.POST.get('fechaP'),formato)
                    partid.fecha=fecha
                partid.numPartida=numPartida
                partid.codEmpresa=emp
                if request.POST.get('concepto'):
                    partid.concepto=request.POST.get('concepto')
                partid.save()   
                # finaliza el registro de partida
                # comienza el registro de movimientos
                for i in range(d):
                    movimient=movimiento()
                    movimient.idPartida=partid
                    cuent=cuenta.objects.get(idCuenta=(int(a[i])))
                    movimient.idCuenta=cuent
                    if b[i]:
                        movimient.debe=float(b[i])
                    if c[i]:
                        movimient.haber=float(c[i])
                    movimient.save()
            #finaliza el  registro de movimientos          
            except Exception:
                ok=False
            
            if ok:
                return render(request,'Registros/Registro.html',{'msg': 'ingreso exitoso','empresa': emp})
               
            else:
                return render(request,'Registros/Registro.html',{'msg': 'Ingreso fallido','empresa': emp})