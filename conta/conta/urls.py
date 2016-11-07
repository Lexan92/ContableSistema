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
from contapp.views import loginRender,importar,gestionEmpresa,queryCatalogo,Catalogo,Registro
# from contapp.views import CrearImportarArchivoView,loginRender,importa

urlpatterns = [
	# url(r'^contapp/', include('contapp.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^conta/home/$', loginRender, name="login",),
    url(r'^conta/Importacion/$', importar, name="importar-nuevo",),
    url(r'^conta/GestionEmpresa/$', gestionEmpresa, name="gestionEmpresa",),
    url(r'^conta/Catalogo/', Catalogo, name="Catalogo",),
    url(r'^conta/Registro/', Registro, name="Registro",),
    #url(r'^conta/Catalogo/', queryCatalogo, name="queryCatalogo",),
    url(r'^conta/Catalogo/consulta', queryCatalogo, name="queryCatalogo",),
    # url(r'^conta/Importacion/$', CrearImportarArchivoView.as_view(), name="importar-nuevo",),
    # url(r'^Medicamentos/Login/$', loginRender, name="login",),
    # url(r'^$', CrearImportarArchivoView.as_view(), name="importar-nuevo",),
    
    # url(r'conta/home/^$', CrearImportarArchivoView.as_view(), name="importar-nuevo",),
]
