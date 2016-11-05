
from contapp.models import  empresa, tipCuenta, rubCuenta, cuenta, partida, movimiento,impArchivo
from datetime import datetime, date, time, timedelta
from django import forms

class FormEmpresa(forms.Form):
    NOMBRE = forms.CharField()
    NIT= forms.CharField()
    NRC= forms.CharField()

class FormImportacion(forms.Form):
    archivo = forms.FileField()



class CatalogoCuentas:

    def __init__(self, empresa):
        self.empresa = empresa
      #esta funcion recursiva recibe una cuenta de mayor y crea uan lista con todas sus subcuentas 
    def newCatalogo(self):
        for i in range(6):
            tipo=tipCuenta()
            tipo.codTipo=i+1
            tipo.codEmpresa=self.empresa
            if i==0:
                tipo.nomTipo="ACTIVO"        
            elif i==1:
                tipo.nomTipo="PASIVO"
            elif i==2:
                tipo.nomTipo="PATRIMONIO"
            elif i==3:
                tipo.nomTipo="CUENTAS DE RESULTADOS DEUDORAS"
            elif i==4:
                tipo.nomTipo="CUENTAS DE RESULTADO ACREEDORAS"
            elif i==5:
                tipo.nomTipo="CUENTA LIQUIDADORA DE RESULTADOS"
            tipo.save()

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
    def cuentasPorRubro(self,rubro):
        lst=[]
        lst.append(rubro)
        if not rubro.getCuentasMayor():
            return lst
        else:
            for c in rubro.getCuentasMayor():
                l=self.listCuentasMenor(c)
                lst=lst+l
            return lst
    def cuentasPorTipo(self,tipo):
        lst=[]
        lst.append(tipo)
        if not tipo.getRubros():
            return lst
        else:
            for r in tipo.getRubros():
                l=self.cuentasPorRubro(r)
                lst=lst+l
            return lst
    def getCatalogo(self):
        ctl=[]
        if not self.empresa.getTipos():
            return ctl
        else:

            for t in self.empresa.getTipos():
                l=self.cuentasPorTipo(t)
                # print(l)
                ctl=ctl+l
                # print(ctl)
            return ctl

class errores():
    archivo = ""
    linea = 0#models.IntegerField()
    mensaje = ""#models.CharField(max_length=500, widget=forms.Textarea)
    tipo = ""#models.CharField(max_length=30)

class ImpCatalago:#name:importar catalogo
    # condiciones de importacion:
    # el archivo debera contener dos columnas separadas por comas si se trabajare en bloc de notas,
    # si se trabajare en excel guardar archivo con formato ".csv/separado por comiilas"
    # la columna 1 tendra el codigo de la cuenta y se denotaran de la siguiente manera:
    # a)los rubros se compondran por dos caracteres el 1ero sera la clase de cuenta q pertecen el 2do sera su codigo correlativo
    # b)las cuantas tendran 1ero el rubro y 2do su codigo correlativo, cabe alclarar que todos los codigos deben tener una cantidad par de caracteres
    #      de otra forma esto causara error por ejemplo 11001 no es un codigo valido pero silo es 111010 o 21010110
    # esto se debe a que un rubro no tendra mas de 99 cuentas y una cuenta no tendra mas de 99 subcuentas y asi 
    # sucesivamente
    #la 2da columna solo contendra el nombre de la cuenta
    
    #resive un string con el codigo de cuenta y lo particiona para crear las dependencias y codigo de cuenta
    #no se permiten codigos con longitud impar sino dara error la insercion 
    def __init__(self, empresa,archivo,nomArchivo):
        # self.empres = empresa()
        self.empresa=empresa
        self.archivo=archivo
        self.err=errores()
        self.err.archivo=nomArchivo


    def conCodigo(self,s):#name:convertir codigo
        #se supone q "s " sea un string 
        #si la longitud de codigo no es par entonces es impar y por ende no hara 
        if ((len(s)%2)==0):#si el residuo es cero entonces el estrin es de una longitud par
            ls=[]
            l=len(s)//2#toma el valor del cociente de "/" este valor nos dira cuantos pares de caracteres existen 
            lm=0#limite menor
            lM=2#limite mayor
            for i in range(l):
                a=s[lm:lM]
                ls.append(a)
                lm=lM
                lM=lM+2
            return ls#c es una lista de strings( de 2 carateres por cada elemento en la list) que posteriormente se convertiran a enteros
       # else:    
        #    ls=""
         #   return ls
  
   
    def creRubro(self,objTupla):#name:crear Rubro
        #si el codigo es de longitud impar osea r[1] no existe, este problema generara una execpcion
        c=objTupla[0]
        ls=self.conCodigo(c)#ls es una lista con un string en este caso 
        r=ls.pop()#"r" contiene el strin del codigo a trocear para verificar si el "tipo" al q pertenece existe y si ese rubro ya existe
        codtipo=int(r[0])#se obtiene el codTipo y se convierte en int ya q era un caracter
        codrubro=int(r[1])#se obtiene el codRubro y se convierte en int ya q era un caracter
        if self.empresa.getTipo(codtipo):#si el tipo existe se procede con lo siguiente
            if not self.empresa.getTipo(codtipo).getRubro(codrubro):#si el rubro no exite procede a crearlo
                R=rubCuenta()
                R.codRubro=codrubro
                R.nomRubro=objTupla[1]
                R.idTipo=self.empresa.getTipo(codtipo)
                R.save()                
        
    def creCuenta(self,objTupla):#name:crear Rubro
        c=objTupla[0]
        ls=self.conCodigo(c)
        r=ls.pop(0)#se hace pop al primer elemento de la list ,"r" contiene el strin del codigo a trocear para verificar si el "tipo" al q pertenece existe y si ese rubro ya existe
        codtipo=int(r[0])#se obtiene el codTipo y se convierte en int ya q era un caracter
        codrubro=int(r[1])#se obtiene el codRubro y se convierte en int ya q era un caracter
        cod=ls.pop()#se hace pop al ultimoelemento de la list, obtine el codCuenta a crear si cumple las demas condiciones
        tipo=self.empresa.getTipo(codtipo)
        rubro=tipo.getRubro(codrubro)
        listC=rubro.getCuentas()#contiene todas las cuentas del rubro identificado
        #si la rubro esta vacia quiere decir q el tipo o el rubro no existe
        
        if rubro:
            if not ls:#si esto es cierto la cuenta a insertar es de mayor
               # cod=int(cod)#se convierte el strin en entero
                c1=""#nos servira para validar si existe o no la cuenta
                for c in listC:#este ciclo comprobara si existe la cuenta q se quiere importar
                    if c.getCodCuenta()==(r+cod):
                    # if c.codCuenta==cod:#si algun codigo de cuenta coincide es porque, ya existe dicha cuenta 
                        c1=c#se asiganara a "c1" la cuenta si ya existiere
                if not c1:#c1 sera vacio si no existe la cuenta a importar y por
                    nc=cuenta()#se creara la nueva cuenta de mayor con todos los paarametros
                    nc.codCuenta=int(cod)
                    nc.nomCuenta=objTupla[1]
                    nc.grado=1
                    nc.idRubro=rubro
                    nc.save()
            #aclaracion la comparacion en el if anterior fue comparando enteros, en esta ocasion sera comparando strings
            else:#ls entonces contiene el codigo del padre troceado
                cp=""#nos servira para validar si existe o no la cuenta padre
                c1=""#nos servira para validar si existe o no la cuenta a importar
                codpadre=""
                for i in ls:#con este for volvere a unir el codigo en un solo string
                    codpadre=codpadre+i  
          
                for c in listC:#se procera a conparar el codigo de cada cuenta con el del codPadre para identificar si el padre existe
                    if c.getCodCuenta()==(r+codpadre):#(r+cod) contiene el codigo de la cuenta q esta formado por rubro+codCuent
                        cp=c# cp tomara el padre si existe

                for c in listC:#este for nos servira para verificar si la cuanta a importar ya existe
                    if c.getCodCuenta()==(r+codpadre+cod):#(r+codpadre+cod) contiene el codigo de la cuenta q se desea importar y la cual se vericara si exista o no
                        c1=c# c1 tomara la cuenta si exite
                cod=int(cod)#se convierte el strin en entero
                if cp:#si es cierto entonces el padre existe
                    if not c1:#c1 sera vacio si no existe la cuenta a importar y
                        nc=cuenta()#se creara la nueva cuenta de menor con todos los paarametros
                        nc.codCuenta=cod
                        nc.nomCuenta=objTupla[1]
                        nc.grado=len(ls)+1
                        nc.idRubro=rubro
                        nc.idCuentaPadre=cp
                        nc.save()
        
    #objeto tupla es la linea de importacion q contiene el codigo y nombre de la cuenta, del achivo importado
    def evaCodigo(self,objTupla):#name:evaluacion de codigo ,evalua el codigo para saber q objeto se creara si cuenta o rubro
        c=objTupla[0]
        ls=self.conCodigo(c)
        if len(ls)==1:#si esto es cierto entonces la lista solo tiene 1 elemento de dos carateres
           self.creRubro(objTupla)#se confirmoq se creara un rubro
        else:#de lo acontraio la lista tiene mas de 1 elemento 
            self.creCuenta(objTupla)#entonces se creara una cuenta o subcuenta si cumple las condiciones
    
    # def importar(self):
    #     try:
    #         for objTupla in self.archivo:
    #             self.err.linea=self.err.linea+1
            
    #             self.evaCodigo(objTupla) 
    #     except Exception as exc:
    #         self.err.mensaje = exc.args
    #         self.err.tipo = type(exc)                   
    #     return self.err                
    def importar(self):
        for objTupla in self.archivo:
            self.evaCodigo(objTupla) 
          
