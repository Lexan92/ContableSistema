---------------funcion por anio y mes----------------------
SELECT "idCuenta_id","idPartida","idMovimiento",fecha,"codCuenta","nomCuenta",concepto,"numPartida","debe","haber" 
FROM contapp_partida a  
inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
inner JOIN contapp_cuenta c ON (b."idCuenta_id"=c."idCuenta") where b."idCuenta_id"=298 
and TO_CHAR(fecha,'YYYY')='2016' and TO_CHAR(fecha,'MM')='11';
/*-------------------------------------------------------------------------------------*/

---------------------------------------bloque que tre hijo ini--------------------------
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") AS (
	SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
	/*-aplica filtro  "idCuenta"=285 para traer hijo y nietos de cualquier cuenta 
	de tenerlos*/
	 FROM contapp_cuenta WHERE   "idCuenta"=289 
      UNION
	SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
	 FROM contapp_cuenta as ms, metas
	  WHERE metas."idCuenta" =ms."idCuentaPadre_id"
	  )


SELECT * FROM metas order by "idCuenta" ;

/*----------------------------------bloque que tra hijo fin--------------------------------------*/



/*--------------------bloq de consulta de movimientos de cualquier cuenta  ---------------------*/
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") AS (
	SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
	/*-aplica filtro  "idCuenta"=285 para traer hijo y nietos de cualquier cuenta 
	de tenerlos*/
	 FROM contapp_cuenta WHERE   "idCuenta"=287
	 ---285 
      UNION
	SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
	 FROM contapp_cuenta as ms, metas
	  WHERE metas."idCuenta" =ms."idCuentaPadre_id"
	  )


--SELECT * FROM metas order by "idCuenta" ;


-------en el select declaro  q columnas necesito para mostrar-----
select * from (SELECT "idCuenta","idPartida","idMovimiento",fecha,"codCuenta","nomCuenta",concepto,"numPartida","debe","haber" 
FROM contapp_partida a  
inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")

		/*	este inner hace launion solo con las cuentas q tienen movimientos
			inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta") 
		*/
inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta") 
          ----------------aplicando filtro de anio y mes--------------------------
--where  TO_CHAR(fecha,'YYYY')='2016' and TO_CHAR(fecha,'MM')='11';
				--1era prueba solo anio--
--where  TO_CHAR(fecha,'YYYY')='2016'
				--2da prueba  anio y mes--
where  TO_CHAR(fecha,'YYYY')='2016' and TO_CHAR(fecha,'MM')='11'
	) s order by s.fecha,s."idCuenta" ;
/*----------------------- fin bloq de consulta de movimiento de cualquier cuenta---------------------*/


/*--------------------bloq de consulta de movimientos de cualquier cuenta produccion  ---------------------*/
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") AS (
	SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
	 FROM contapp_cuenta WHERE   "idCuenta"=298 
      UNION
	SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
	 FROM contapp_cuenta as ms, metas
	  WHERE metas."idCuenta" =ms."idCuentaPadre_id"
	  )
select * from (SELECT "idMovimiento",fecha
FROM contapp_partida a  
inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")		
inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta")         
where  TO_CHAR(fecha,'YYYY')='2016' and TO_CHAR(fecha,'MM')='11'
	) s order by s.fecha ;
/*----------------------- fin bloq de consulta de movimiento de cualquier cuenta---------------------*/


WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") AS (
	SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
	 FROM contapp_cuenta WHERE   "idCuenta"=287 
      UNION
	SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
	 FROM contapp_cuenta as ms, metas
	  WHERE metas."idCuenta" =ms."idCuentaPadre_id"
	  )
-------en el select declaro  q columnas necesito para mostrar-----
select sum(sl."debe") as debe,sum(sl."haber") as haber  from (select * from (SELECT "idCuenta","idPartida","idMovimiento",fecha,"codCuenta","nomCuenta",concepto,"numPartida","debe","haber" 
FROM contapp_partida a  
inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta") 
where  TO_CHAR(fecha,'YYYY')='2016' and TO_CHAR(fecha,'MM')='11'
	) s order by s.fecha,s."idCuenta") sl ;
/*----------------------- fin bloq de consulta de movimiento de cualquier cuenta---------------------*/

/*-------------------------------------obtengo saldos de una cuenta en debe y haber------------------------------------------------*/
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") AS (
	SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
	 FROM contapp_cuenta WHERE   "idCuenta"=312 
      UNION
	SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
	 FROM contapp_cuenta as ms, metas
	  WHERE metas."idCuenta" =ms."idCuentaPadre_id"
	  )

select sum(sl."debe") as debe,sum(sl."haber") as haber  from (
select * 
from (SELECT "idMovimiento",fecha,"debe","haber" 
FROM contapp_partida a  
inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta") 
where  TO_CHAR(fecha,'YYYY')='2016' and TO_CHAR(fecha,'MM')='11'
	) s order by s.fecha) sl ;
/*----------------------- fin bloq de consulta de saldos de debe y haber cuenta---------------------*/


/*-------------------------------------obtengo saldo de una cuenta ------------------------------------------------*/
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") AS (
	SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
	 FROM contapp_cuenta WHERE   "idCuenta"=287 
      UNION
	SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
	 FROM contapp_cuenta as ms, metas
	  WHERE metas."idCuenta" =ms."idCuentaPadre_id"
	  )

select (sum(sl."debe") - sum(sl."haber") ) as saldo  from (
select * 
from (SELECT "idMovimiento",fecha,"debe","haber" 
FROM contapp_partida a  
inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta") 
where  TO_CHAR(fecha,'YYYY')='2016' and TO_CHAR(fecha,'MM')='11'
	) s order by s.fecha) sl ;
/*----------------------- fin bloq de consulta de saldo de  cuenta---------------------*/






/*saldos acreedores*/
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id")
                AS (SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
                FROM contapp_cuenta WHERE   "idCuenta"=287
                UNION
                SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
                FROM contapp_cuenta as ms, metas WHERE metas."idCuenta" =ms."idCuentaPadre_id"
                )
                select (sum(sl."haber") - sum(sl."debe")) saldo from (
                    select * from (SELECT "idMovimiento",fecha,"debe","haber"
                    FROM contapp_partida a
                    inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
                    inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta")
                    where  TO_CHAR(fecha,'YYYY')='2016' and TO_CHAR(fecha,'MM')='11')
                    s order by s.fecha) 
                sl




/*saldos deudores*/
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id")
                AS (SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
                FROM contapp_cuenta WHERE   "idCuenta"=312
                UNION
                SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
                FROM contapp_cuenta as ms, metas WHERE metas."idCuenta" =ms."idCuentaPadre_id"
                )
                select (sum(sl."debe") - sum(sl."haber")) saldo from (
                    select * from (SELECT "idMovimiento",fecha,"debe","haber"
                    FROM contapp_partida a
                    inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
                    inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta")
                    where  TO_CHAR(fecha,'YYYY')='2016' and TO_CHAR(fecha,'MM')='11')
                    s order by s.fecha) 
                sl

