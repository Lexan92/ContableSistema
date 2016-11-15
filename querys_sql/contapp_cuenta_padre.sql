SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
  FROM public.contapp_cuenta;
SELECT *  FROM public.contapp_cuenta where "idCuentaPadre_id" isnull ;
SELECT *  FROM public.contapp_cuenta as p where p."idCuentaPadre_id" isnull ;
SELECT *  FROM public.contapp_cuenta as p where p.grado=3 ;

SELECT *  FROM contapp_cuenta as p where "idCuentaPadre_id" isnull and "idRubro_id"=8 and "codCuenta"=p."idCuentaPadre_id";

-- primera linea que crea la tabla (no sé como llamarla ) con las columnas que necesito
---------------------------------------bloque que trae hijo ini--------------------------
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") AS (
	SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
	/*este bloque te trae todas las cuentas de mayor y menor por rubro
		*/
	 FROM contapp_cuenta WHERE "idCuentaPadre_id" isnull and "idRubro_id"=8 
      UNION
	SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
	 FROM contapp_cuenta as ms, metas
	  WHERE metas."idCuenta" =ms."idCuentaPadre_id"
	  )


SELECT * FROM metas order by "idCuenta" ;
----------------------------------bloque que trea hijo fin--------------------------------------------

SELECT *  FROM public.contapp_cuenta as p where "idCuenta"=285 ;


---------------------------------------bloque que tre hijo ini--------------------------
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") AS (
	SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
	/*-aplica filtro "idCuentaPadre_id" isnull and  "idCuenta"=285 para saber sila cuenta 
	 es mayor y devlovera hijos y nietos de tenerlos
	 este bloque te trae una cuenta mayor con todos los hijos*/
	 FROM contapp_cuenta WHERE "idCuentaPadre_id" isnull and  "idCuenta"=285 
      UNION
	SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
	 FROM contapp_cuenta as ms, metas
	  WHERE metas."idCuenta" =ms."idCuentaPadre_id"
	  )


SELECT * FROM metas order by "idCuenta" ;
------variante codcuenta-----------------este
----------------------------------bloque que tra hijo fin--------------------------------------------

---------------------------------------bloque que tre hijo ini--------------------------
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") AS (
	SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
	/*-aplica filtro  "idCuenta"=285 para traer hijo y nietos de cualquier cuenta 
	de tenerlos*/
	 FROM contapp_cuenta WHERE   "idCuenta"=297 
      UNION
	SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
	 FROM contapp_cuenta as ms, metas
	  WHERE metas."idCuenta" =ms."idCuentaPadre_id"
	  )


SELECT * FROM metas order by "idCuenta" ;
----------------------------------bloque que tra hijo fin--------------------------------------------

