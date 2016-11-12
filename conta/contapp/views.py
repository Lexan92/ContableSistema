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

def queryCatalogo(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""    
    if emp:
        return render(request,"Catalogo/importExito.html",{'empresa': emp}) 
    



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


# class CrearImportarArchivoView(CreateView):
#     model = impArchivo
#     template_name = 'ImportarArchivo.html'
#     fields = ['date', 'codEmpresa','archivo'] #'__all__' #['anio', 'idZona']
#     #ya importa y guarda
#     def form_valid(self,form):
#     	if self.request.method == 'POST':
#             if self.request.session.has_key('codemp'):
#                 usr = usuario.objects.get(idUsuario = int(self.request.session['usuario']))
#             #archivo importado
#                 form=impArchivo()
#                 empres=empresa.objects.get(codEmpresa=(int(self.request.POST.get('codEmpresa'))))
#                 form.codEmpresa=empres
#                 form.archivo=self.request.FILES.get('archivo')
#                 form.date=self.request.POST.get('date')
#                 form.save()
#                 dataReader = csv.reader(open(UPLOAD_FOLDER + "/" + str(form.archivo)), delimiter=',', quotechar='"')
#                 nombreArchivo=str(form.archivo)#self.request.FILES["archivo"].name 
#                 catalogoImportado=ImpCatalago(empres,dataReader,nombreArchivo)
#                 catalogoImportado.importar()
#                 ordenCat=CatalogoCuentas(empres)
#                 return render(self.request,'importExito.html',{'cat': ordenCat})
#             elif self.request.session.has_key('codemp') == False: #Usuario no ha iniciado sesión
#                 return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresar para iniciar','empresas':empresa.objects.all(),})
#                 #return render(self.request,"IniciarSesion.html", {'mensaje': 'Debe selecionar una empresar para iniciar'})    
#             # errorC=catalogoImportado.importar()
            
#             # if (not errorC.mensaje) and  (not errorC.tipo):
#             #     return render(self.request,'tabla_dinamica.html')
#             # else:
#             #
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
            # d=[]
            # d.append(len(a))
            # d.append(len(b))
            # d.append(len(c))
            d=len(a)
            formato = "%Y-%m-%d"                  
            

            # fecha=request.POST.get('fechaP')
            numPartida=request.POST.get('numeroP')
            # comienza registro de partida
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
                    movimient.debe=int(b[i])
                if c[i]:
                    movimient.haber=int(c[i])
                movimient.save()
            #finaliza el  registro de movimientos

            partidas=partida.objects.filter(codEmpresa=emp.codEmpresa) 
            if partidas:
                # return render(request,'Registros/Registro.html',{'msg': 'ingreso exitoso','empresa': emp})
                return render(request,'Registros/msgPartida.html',{'msg': 'ya casi man','partidas': partidas})
                # return render(request,'Registros/msgPartida.html',{'msg': 'ya casi man','partidas': partidas})
                # return render(request,'msgPartida.html',{'msg': 'ya casi man','cod': a,'debe': b,'haber': c,'long': d,'partidas': partidas})
            else:
                return render(request,'Registros/msgPartida.html',{'msg': 'no hay registros'}) 	

def Empresa(request):
    return render(request,'ErrorMigracion.html')

def Catalogo(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""
    if emp:
        return render(request,'Catalogo/Catalogo.html')
            
 
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
   


    

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
