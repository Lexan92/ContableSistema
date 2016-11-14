import os
import csv
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, time, timedelta
from contapp.models import  *
# from contapp.models import  empresa, tipCuenta, rubCuenta, cuenta, partida, movimiento,impArchivo
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
        return render(request,"Catalogo/Catalogo.html")

def consultaCatalogo(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""    
    if emp:
        return render(request,"Catalogo/consultaCatalogo.html",{'empresa': emp}) 



def createUpdateC(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""
    if request.method == 'POST':
        if request.session.has_key('codemp'):
            cuent=cuenta()
            rubro=rubCuenta.objects.get(idRubro=int(request.POST.get('idrubro')))
            cuent.idRubro=rubro
            
            if request.POST.get('idpadre'):
                cuentaDad=cuenta.objects.get(idCuenta= int(request.POST.get('idpadre')))
                cuent.idCuentaPadre=cuentaDad
            cuent.grado=(int(request.POST.get('grado')))
            cuent.codCuenta=(int(request.POST.get('codnext')))
            nombreCuenta=request.POST.get('nombreCuenta')
            cuent.nomCuenta=nombreCuenta
            cuent.save()
            mensaj="ingerso exitoso"
            return render(request,'Catalogo/createUpdate.html',{'mensaje': mensaj,'empresa': emp})

        elif request.session.has_key('codemp') == False: #Usuario no ha iniciado sesión
            return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresar para iniciar','empresas':empresa.objects.all(),})
            # confirma si  existe una sesioncon una empresa
    elif emp:
        return render(request,'Catalogo/createUpdate.html',{'empresa': emp})
    else:
        return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresa para iniciar','empresas':empresa.objects.all(),})    

def confirmarcreate(request):

    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""

    if request.method == 'POST':
        if request.session.has_key('codemp'):
            # newcuent=cuenta()
            try:
                cuentaDad=cuenta.objects.get(idCuenta= int(request.POST.get('idPadre')))
            except Exception :
                cuentaDad=""
            try:
                rubro=rubCuenta.objects.get(idRubro=int(request.POST.get('idRubro')))
            except Exception :
                mensaj="rubro no existe, ingerso fallido"
                return render(request,'Catalogo/createUpdate.html',{'mensaje': mensaj,'empresa': emp})
            
            if cuentaDad :
                if (cuentaDad.haveMoves()):
                    mensaj="cuenta padre posee movimientos, cuenta padre no debe tener movientos, ingerso fallido"
                    return render(request,'Catalogo/createUpdate.html',{'mensaje': mensaj,'empresa': emp})
                codnext_str=(cuentaDad.getCodCuenta())+(cuentaDad.getCodNextSon_str())
                codnext=(cuentaDad.getCodNextSon())
                
                grado=(cuentaDad.grado)+1
            else:
                codnext_str=(rubro.getCodRubro())+(rubro.getCodNextMayor_str())#formato de proximo codigo Strin
                codnext=(rubro.getCodNextMayor())#formato de proximo codigo int
                grado=1

            if rubro and cuentaDad:
                if not cuentaDad.idRubro.idRubro==rubro.idRubro:
                    mensaj="rubro no corresponde a rubro de cuenta padre, ingreso fallido"
                    return render(request,'Catalogo/createUpdate.html',{'mensaje': mensaj,'empresa': emp})
            nombreCuenta=request.POST.get('nombreCuenta')
            return render(request, "Catalogo/afirmarCreate.html", 
                {'codnext_str':codnext_str,
                'codnext':codnext,
                'nomcuenta':nombreCuenta,
                'grado':grado,
                'rubro':rubro,
                'dad':cuentaDad,
                'empresa': emp,})
        
        elif request.session.has_key('codemp') == False: #Usuario no ha iniciado sesión
            return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresar para iniciar','empresas':empresa.objects.all(),})
    # confirma si  existe una sesioncon una empresa
    elif not emp:
        return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresa para iniciar','empresas':empresa.objects.all(),})
        
 



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
