from django.contrib import admin
from contapp.models import  empresa, tipCuenta, rubCuenta, cuenta, partida, movimiento
# Register your models here.

# class FechaAdmin(admin.ModelAdmin):eliminado del modelo
	# list_display = ('idFecha', 'dia','mes','anio','fechaOpc') #tupla

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('codEmpresa','nomEmpresa','nit','nrc')

class TipCuentaAdmin(admin.ModelAdmin):
	list_display = ('idTipo','codTipo','nomTipo','codEmpresa')

class RubCuentaAdmin(admin.ModelAdmin):
	list_display = ('idRubro','codRubro','nomRubro','idTipo')

class CuentaAdmin(admin.ModelAdmin):
	list_display = ('idCuenta', 'codCuenta', 'nomCuenta', 'grado', 'idRubro', 'idCuentaPadre')

class PartidaAdmin(admin.ModelAdmin):
	list_display = ('idPartida', 'numPartida','codEmpresa','fecha')

class MovimientoAdmin(admin.ModelAdmin):
	list_display = ('idMovimiento','debe','haber','idPartida') #errorr en nombre de id


# admin.site.register(fecha,FechaAdmin)
admin.site.register(empresa,EmpresaAdmin)
admin.site.register(tipCuenta,TipCuentaAdmin)
admin.site.register(rubCuenta,RubCuentaAdmin)
admin.site.register(cuenta,CuentaAdmin)
admin.site.register(partida,PartidaAdmin)
admin.site.register(movimiento,MovimientoAdmin)