"""conta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
# from contapp.views import *
from contapp.viewsCatalogo import *
from contapp.viewsEstadosF import *
from contapp.viewsEmpresa import *
from contapp.viewsLibros import *
from contapp.viewsRegistro import *
# from contapp.views import loginRender,importar,gestionEmpresa,queryCatalogo,Catalogo,Registro
# from contapp.views import CrearImportarArchivoView,loginRender,importa

urlpatterns = [
	# url(r'^contapp/', include('contapp.urls')),
    url(r'^admin/', admin.site.urls),


# ----------------------------EMPRESA-------------------------------------------
    url(r'^conta/home/$', loginRender, name="login",),
    url(r'^conta/GestionEmpresa/$', gestionEmpresa, name="gestionEmpresa",),

# ----------------------------REGISTRO-------------------------------------------
    url(r'^conta/Registro/$', Registro, name="Registro",),
    url(r'^conta/Registro/consulta/$', consultaPartida, name="consultaPartida",),
    url(r'^conta/regPartida/$', regPartida, name="regPartida",),

# -----------------------------CATALOGO------------------------------------------
    url(r'^conta/Catalogo/$', Catalogo, name="Catalogo",),
    url(r'^conta/Importacion/$', importar, name="importar-nuevo",),
    url(r'^conta/Catalogo/consulta/$', consultaCatalogo, name="consultaCatalogo",),
    url(r'^conta/Catalogo/GestionCuenta/$', createUpdateC, name="createUpdateC",),
    url(r'^conta/Catalogo/GestionCuenta/confirmar/$', confirmarcreate, name="confirmarcreate",),


#------------------------------LIBROS--------------------------------------------
    url(r'^conta/Libros/$', Libros, name="Libros",),
    url(r'^conta/Libros/Consulta/$', consultaLibro, name="consultaLibro",),
#-------------------------ESTADOS FIANANCIEROS-----------------------------------
    url(r'^conta/EstadosFinancieros/$', estadosF, name="estadosF",),
     url(r'^conta/EstadosFinancieros/Consulta$', consultaEstadoF, name="consultaEstadoF",),

    # url(r'^conta/Catalogo/', queryCatalogo, name="queryCatalogo",),
    
    # url(r'^conta/Registro/consulta/', consultaPartidas, name="consultaPartidas",),
    # url(r'^conta/Importacion/$', CrearImportarArchivoView.as_view(), name="importar-nuevo",),
    # url(r'^Medicamentos/Login/$', loginRender, name="login",),
    # url(r'^$', CrearImportarArchivoView.as_view(), name="importar-nuevo",),
    
    # url(r'conta/home/^$', CrearImportarArchivoView.as_view(), name="importar-nuevo",),
]
