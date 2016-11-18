

                
/*------------------CONSULTA SALDOS EN DEBE Y HABER DE RUBRO COMPLETO ACUMULADO(POR AÑO)--------------------------------------------------------*/
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") 
                AS (select *from (SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
                FROM contapp_cuenta WHERE  "idRubro_id"=7 order by "idCuenta") as rc
                UNION
                SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
                FROM contapp_cuenta as ms, metas WHERE metas."idCuenta" =ms."idCuentaPadre_id"
                )
                select sum(sl."debe") as debe,sum(sl."haber") as haber from (
                    select * from (SELECT "idMovimiento",fecha,"debe","haber"
                    FROM contapp_partida a
                    inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
                    inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta")
                    where  TO_CHAR(fecha,'YYYY')='2016' )
                    s order by s.fecha) 
                sl  
/*----------------------------------------------------------------------------------------*/

/*------------------CONSULTA SALDO(deudor) DE RUBRO COMPLETO ACUMULADO(POR AÑO)--------------------------------------------------------*/
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") 
                AS (select *from (SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
                FROM contapp_cuenta WHERE  "idRubro_id"=7 order by "idCuenta") as rc
                UNION
                SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
                FROM contapp_cuenta as ms, metas WHERE metas."idCuenta" =ms."idCuentaPadre_id"
                )
                select (sum(sl."debe") - sum(sl."haber")) saldo from (
                    select * from (SELECT "idMovimiento",fecha,"debe","haber"
                    FROM contapp_partida a
                    inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
                    inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta")
                    where  TO_CHAR(fecha,'YYYY')='2016' )
                    s order by s.fecha) 
                sl  
/*----------------------------------------------------------------------------------------*/

/*------------------CONSULTA SALDO(acreedor) DE RUBRO COMPLETO ACUMULADO(POR AÑO)--------------------------------------------------------*/
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") 
                AS (select *from (SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
                FROM contapp_cuenta WHERE  "idRubro_id"=7 order by "idCuenta") as rc
                UNION
                SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
                FROM contapp_cuenta as ms, metas WHERE metas."idCuenta" =ms."idCuentaPadre_id"
                )
                select (sum(sl."haber") - sum(sl."debe")) saldo from (
                    select * from (SELECT "idMovimiento",fecha,"debe","haber"
                    FROM contapp_partida a
                    inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
                    inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta")
                    where  TO_CHAR(fecha,'YYYY')='2016' )
                    s order by s.fecha) 
                sl  
/*----------------------------------------------------------------------------------------*/

/*-----------CONSULTA SALDOS EN DEBE Y HABER DE RUBRO COMPLETO POR PERIODO(POR AÑO Y MES)--------------------------------------*/
WITH RECURSIVE metas("idCuenta", "codCuenta", "nomCuenta",grado, "idCuentaPadre_id", "idRubro_id") 
                AS (select *from (SELECT "idCuenta", "codCuenta", "nomCuenta", grado, "idCuentaPadre_id","idRubro_id"
                FROM contapp_cuenta WHERE  "idRubro_id"=7 order by "idCuenta") as rc
                UNION
                SELECT ms."idCuenta", ms."codCuenta",ms."nomCuenta",ms.grado, ms."idCuentaPadre_id", ms."idRubro_id"
                FROM contapp_cuenta as ms, metas WHERE metas."idCuenta" =ms."idCuentaPadre_id"
                )
                select sum(sl."debe") as debe,sum(sl."haber") as haber from (
                    select * from (SELECT "idMovimiento",fecha,"debe","haber"
                    FROM contapp_partida a
                    inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
                    inner JOIN metas c ON (b."idCuenta_id"=c."idCuenta")
                    where  TO_CHAR(fecha,'YYYY')='2016' AND TO_CHAR(fecha,'MM')='09')
                    s order by s.fecha) 
                sl  
/*----------------------------------------------------------------------------------------*/








select cr."idCuenta", cr."codCuenta", cr."nomCuenta", grado, cr."idCuentaPadre_id",cr."idRubro_id"
 from (SELECT * FROM contapp_cuenta a
inner JOIN contapp_rubcuenta b ON (a."idRubro_id"=b."idRubro")) as cr
WHERE cr."idRubro"=7 order by cr."idCuenta"