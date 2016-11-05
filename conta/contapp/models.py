from django.db import models
from datetime import datetime, date, time, timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
# por conveniencia no se manejara la clase fecha sino que usara 

class empresa(models.Model):
    codEmpresa=models.AutoField(primary_key=True)
    nomEmpresa=models.CharField(max_length=100)
    nit=models.CharField(max_length=50)
    nrc=models.CharField(max_length=50)
    def getTipo(self,arg):#busca un tipo de cuenta por empresa y codTipo
        tipo=tipCuenta.objects.filter(codEmpresa=self.codEmpresa).get(codTipo=arg)
        return tipo
    # def getTipo(self,arg):#busca un tipo de cuenta por empresa y codTipo
        # tipo=tipCuenta.objects.filter(codEmpresa=self.codEmpresa).filter(codTipo=arg)
        # return tipo
    def getTipos(self):
        tipos=tipCuenta.objects.filter(codEmpresa=self.codEmpresa).order_by('codTipo')
        return tipos
    def getCodEmp(self):
       return self.codEmpresa
    def getnomEmp(self):
       return self.nomEmpresa
    def getNit(self):
       return self.nit
    def getNrc(self):
       return self.nrc
    def setCodEmp(self,arg):
   	    self.codEmpresa=arg
    def setNomEmp(self,arg):
        self.nomEmpresa=arg
    def setNit(self,arg):
        self.nit=arg
    def setNrc(self,arg):
        self.nrc=arg
    def __str__(self):              # __unicode__ on python 2
        return self.nomEmpresa


class tipCuenta(models.Model):
    idTipo=models.AutoField(primary_key=True)
    codTipo=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(9)])
    nomTipo=models.CharField(max_length=50)
    codEmpresa=models.ForeignKey(empresa, on_delete=models.CASCADE)
    def getRubro(self,rubro):
        try:
            rub=rubCuenta.objects.filter(idTipo=self.idTipo).get(codRubro=rubro)
        except rubCuenta.DoesNotExist:
            rub=""
        return rub
    def getRubros(self):
        rubs=rubCuenta.objects.filter(idTipo=self.idTipo).order_by('codRubro')
        return rubs
    def __str__(self):
        return self.codEmpresa.nomEmpresa+" // "+(str(self.codTipo))+" "+self.nomTipo


class rubCuenta(models.Model):
    idRubro=models.AutoField(primary_key=True)
    codRubro=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(9)])
    nomRubro=models.CharField(max_length=50)
    idTipo=models.ForeignKey(tipCuenta, on_delete=models.CASCADE)
    
    def getCodRubro(self):
        cod=(str(self.idTipo.codTipo))+(str(self.codRubro))
        return cod
    def getCuentasMayor(self):#obtiene las cuantas de mayor q contiene el rubro
        cuentas=cuenta.objects.filter(idRubro=self.idRubro).filter(idCuentaPadre__isnull=True).order_by('codCuenta')
        return cuentas
    def getCuentas(self):#obtiene todas las cuentas q pertenecen al rubro
        cuentas=cuenta.objects.filter(idRubro=self.idRubro).order_by('codCuenta')
        return cuentas
    def listCuentasMenor(self,cuentaPadre):
     #caso base
        cpc=[]
        cpc.append(cuentaPadre)
     #si la cuenta no tiene hijas se retorna la lista solo con la cuenta enviada       
        if not cuentaPadre.getSons():
            return cpc
        else:  
            for c in cuentaPadre.getSons():
                l=self.listCuentasMenor(c)
                cpc=cpc+l
    #si la cuenta tienes hijas se envia una lista con el padre y las hijas y nietos     
            return cpc
    #se obtiene una lista de cuentas por rubro
    def cuentasPorRubro(self):
        lst=[]
        # lst.append(rubro)
        # if not rubro.getCuentasMayor():
        if not self.getCuentasMayor():
            return lst
        else:
            for c in self.getCuentasMayor():
                l=self.listCuentasMenor(c)
                lst=lst+l
            return lst    

    def __str__(self):
        return self.idTipo.codEmpresa.nomEmpresa+" // "+ (str(self.idTipo.codTipo))+(str(self.codRubro))+" "+self.nomRubro


class cuenta(models.Model):
    idCuenta=models.AutoField(primary_key=True)
    codCuenta=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(99)])
    nomCuenta=models.CharField(max_length=200)
    grado=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(9)])
    idRubro=models.ForeignKey(rubCuenta, on_delete=models.CASCADE)
    idCuentaPadre=models.ForeignKey('self',null=True,blank=True)

    def getCod(self):
        if not self.idCuentaPadre:
            cod=(str(self.codCuenta).zfill(2))
            return cod
        else:
            cod=self.idCuentaPadre.getCod()
            return cod+(str(self.codCuenta).zfill(2))   
    def getCodCuenta(self):
        if not self.idCuentaPadre:
            cod=(str(self.codCuenta).zfill(2))
            return (self.idRubro.getCodRubro())+cod
        else:
            cod=self.idCuentaPadre.getCod()
            return (self.idRubro.getCodRubro())+cod+(str(self.codCuenta).zfill(2))  
    def getSons(self):
        sons=cuenta.objects.filter(idCuentaPadre=self.idCuenta).order_by('codCuenta')
        return sons
    def __str__(self):
        return (str(self.idCuenta))+"//"+self.getCodCuenta()+" "+self.nomCuenta
        # return (str(self.idCuenta))+" "+(str(self.codCuenta).zfill(2))+" "+self.nomCuenta


class partida(models.Model):
    idPartida=models.AutoField(primary_key=True)
    numPartida=models.IntegerField()
    codEmpresa=models.ForeignKey(empresa, on_delete=models.CASCADE)
    # idFecha=models.ForeignKey(fecha, on_delete=models.CASCADE)
    fecha=models.DateField(default=datetime.now)
    def getMovs(self):
        movs=movimiento.objects.filter(idPartida=self.idPartida)
        return movs
    def __str__(self):
        return " Partida n: "+str(self.numPartida)



class movimiento(models.Model):
    idMovimiento=models.AutoField(primary_key=True)
    debe=models.FloatField(null=True,blank=True)
    haber=models.FloatField(null=True,blank=True)
    idPartida=models.ForeignKey(partida, on_delete=models.CASCADE)
    idCuenta=models.ForeignKey(cuenta,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return " movimeinto n: "+str(self.idMovimiento)

class impArchivo(models.Model):
    idImpArchivo=models.AutoField(primary_key=True)
    codEmpresa=models.ForeignKey(empresa, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos')
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.codEmpresa.nomEmpresa+" // id de importacion:"+str(self.idImpArchivo)+self.date