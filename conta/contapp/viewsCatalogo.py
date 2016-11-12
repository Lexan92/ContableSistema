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


def Catalogo(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""
    if emp:
        return render(request,'Catalogo/Catalogo.html')

def consultaCatalogo(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""    
    if emp:
        return render(request,"Catalogo/consultaCatalogo.html",{'empresa': emp}) 
    



def importar(request):
    #  el try corrobora, si existe una sesion con una empresa
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""
    # emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    if request.method == 'POST':
        if request.session.has_key('codemp'):
            # usr = usuario.objects.get(idUsuario = int(self.request.session['usuario']))
          #archivo importado
            form=impArchivo()
            # empres=empresa.objects.get(codEmpresa=(int(self.request.POST.get('codEmpresa'))))
            form.codEmpresa=emp
            form.archivo=request.FILES.get('archivo')
            # form.date=self.request.POST.get('date')
            form.save()
            dataReader = csv.reader(open(UPLOAD_FOLDER + "/" + str(form.archivo)), delimiter=',', quotechar='"')
            nombreArchivo=str(form.archivo)#self.request.FILES["archivo"].name 
            catalogoImportado=ImpCatalago(emp,dataReader,nombreArchivo)
            catalogoImportado.importar()
            # ordenCat=CatalogoCuentas(emp)
            return render(request,'Catalogo/importExito.html',{'empresa': emp})
            # return render(request,'importExito.html',{'cat': ordenCat})
        elif request.session.has_key('codemp') == False: #Usuario no ha iniciado sesión
            return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresar para iniciar','empresas':empresa.objects.all(),})
    # confirma si  existe una sesioncon una empresa
    elif emp:
        form = FormImportacion()#formulario para la importacion
        return render(request,'Catalogo/ImportarArchivo.html',{'form': form,'empresa': emp})
    else:
        return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresa para iniciar','empresas':empresa.objects.all(),})    
