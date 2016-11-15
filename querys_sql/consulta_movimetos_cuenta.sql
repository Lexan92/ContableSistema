SELECT * FROM contapp_partida WHERE  TO_CHAR(fecha,'YYYY')='2016' and 
 TO_CHAR(fecha,'MM')='10';
SELECT *  FROM contapp_partida;

SELECT "idPartida"  FROM contapp_partida;
SELECT *  FROM contapp_movimiento ;
SELECT "idPartida_id"  FROM contapp_movimiento where "idPartida_id"=2;

SELECT * FROM contapp_partida a 
JOIN contapp_movimiento b ON ("idPartida"="idPartida_id");

SELECT * FROM contapp_partida a 
JOIN contapp_movimiento b ON ("idPartida"="idPartida_id") where "idCuenta_id"=298;

SELECT "idCuenta_id","idPartida","idMovimiento",fecha,concepto,"numPartida","debe","haber" 
FROM contapp_partida a JOIN contapp_movimiento b 
ON ("idPartida"="idPartida_id") where "idCuenta_id"=298;

SELECT "idCuenta_id","idPartida","idMovimiento",fecha,concepto,"numPartida","debe","haber" 
FROM contapp_partida a 
inner JOIN contapp_movimiento b ON ("idPartida"="idPartida_id") where "idCuenta_id"=298;
/*---------------------------------------------------------------------------------*/
----v1------------------------------------------------------------------
SELECT *
FROM contapp_partida  
inner JOIN contapp_movimiento  ON ("idPartida"="idPartida_id")
inner JOIN contapp_cuenta  ON ("idCuenta_id"="idCuenta") where "idCuenta_id"=298;
-----------------v2---------------------------------------------------
SELECT *
FROM contapp_partida a 
inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
inner JOIN contapp_cuenta c ON (b."idCuenta_id"=c."idCuenta") where b."idCuenta_id"=298;
-----------------v22---------------------------------------------------
SELECT *
FROM contapp_partida a 
inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
inner JOIN contapp_cuenta c ON (b."idCuenta_id"=c."idCuenta") where b."idCuenta_id"=298;

/*-------------------------------------------------------------------------------------*/
---------------la actual y funcionl por anioo y mes----------------------
SELECT "idCuenta_id","idPartida","idMovimiento",fecha,"codCuenta","nomCuenta",concepto,"numPartida","debe","haber" 
FROM contapp_partida  
inner JOIN contapp_movimiento  ON ("idPartida"="idPartida_id")
inner JOIN contapp_cuenta  ON ("idCuenta_id"="idCuenta") where "idCuenta_id"=298 
and TO_CHAR(fecha,'YYYY')='2016' and TO_CHAR(fecha,'MM')='11';

---------------funcion por anio y mes----------------------
SELECT "idCuenta_id","idPartida","idMovimiento",fecha,"codCuenta","nomCuenta",concepto,"numPartida","debe","haber" 
FROM contapp_partida a  
inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
inner JOIN contapp_cuenta c ON (b."idCuenta_id"=c."idCuenta") where b."idCuenta_id"=298 
and TO_CHAR(fecha,'YYYY')='2016' and TO_CHAR(fecha,'MM')='11';

---------------la actual y funcionl por anio--v1--------------------
SELECT "idCuenta_id","idPartida","idMovimiento",fecha,"codCuenta","nomCuenta",concepto,"numPartida","debe","haber" 
FROM contapp_partida  
inner JOIN contapp_movimiento  ON ("idPartida"="idPartida_id")
inner JOIN contapp_cuenta  ON ("idCuenta_id"="idCuenta") where "idCuenta_id"=298 
and TO_CHAR(fecha,'YYYY')='2016';
------------------la actual y funcionl por anio-v2-------------------------
SELECT "idCuenta_id","idPartida","idMovimiento",fecha,"codCuenta","nomCuenta",concepto,"numPartida","debe","haber" 
FROM contapp_partida a  
inner JOIN contapp_movimiento b ON (a."idPartida"=b."idPartida_id")
inner JOIN contapp_cuenta c ON (b."idCuenta_id"=c."idCuenta") where b."idCuenta_id"=298 
and TO_CHAR(fecha,'YYYY')='2016';

----otra forma---------
SELECT "idCuenta_id","idPartida","idMovimiento",fecha,"codCuenta","nomCuenta",
concepto,"numPartida","debe","haber" 
FROM contapp_partida , contapp_movimiento ,contapp_cuenta   
where ("idPartida"="idPartida_id") and ("idCuenta_id"="idCuenta") and "idCuenta_id"=298;


SELECT "b1.idCuenta_id" 
FROM contapp_partida as a1,contapp_movimiento as b1,contapp_cuenta as c1  
where ("a1.idPartida"="b1.idPartida_id") and ("b1.idCuenta_id"="c1.idCuenta") and "b1.idCuenta_id"=298;


------da error--------
SELECT "idCuenta_id","idPartida","idMovimiento",fecha,"codCuenta","nomCuenta",concepto,"numPartida","debe","haber" 
FROM contapp_partida a 
inner JOIN contapp_movimiento b ON ("idPartida"="idPartida_id")
inner JOIN contapp_cuenta c ON ("idCuenta_id"="idCuenta")
inner JOIN contapp_cuenta d ON ("c_idCuenta"="d.idCuentaPadre_id") where "idCuenta_id"=298;
