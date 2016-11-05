import os
import csv
from django.shortcuts import render
from django.http import HttpResponse
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
        return render(request, "gestionEmpresa.html", {'form': form})    

def queryCatalogo(request):
    try:
        emp = empresa.objects.get(codEmpresa = int(request.session['codemp']))
    except Exception :
        emp=""    
    if emp:
        return render(request,'importExito.html',{'empresa': emp}) 
    



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
            return render(request,'importExito.html',{'empresa': emp})
            # return render(request,'importExito.html',{'cat': ordenCat})
        elif request.session.has_key('codemp') == False: #Usuario no ha iniciado sesión
            return render(request, "Home.html", {'mensaje': 'Debe selecionar una empresar para iniciar','empresas':empresa.objects.all(),})
    # confirma si  existe una sesioncon una empresa
    elif emp:
        form = FormImportacion()#formulario para la importacion
        return render(request,'ImportarArchivo.html',{'form': form,'empresa': emp})
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
#             # 	return render(self.request,'ErrorMigracion.html', {'err': errorC})
       





def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
