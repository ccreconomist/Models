
SELECT YEAR(Fecha_Solicitud) AS ANIO, MONTH(Fecha_Solicitud) AS MES,  A.Id_Socio, B.Dsc_Socio AS SOCIO, COUNT(DISTINCT A.Case_Number) AS TRAMITES
, Dsc_Producto
FROM Tabla_Captura_Rapida_DatosBasicos  AS A 
INNER JOIN Cat_Socios AS B ON A.Id_Socio = B.Id_Socio 
	AND Fecha_Solicitud >= '2023-06-01 00:00:00' 
	AND Fecha_Solicitud < '2023-10-10 00:00:00' 
AND A.Id_Socio  IN('0') 
GROUP BY YEAR(Fecha_Solicitud), MONTH(Fecha_Solicitud),  A.Id_Socio, B.Dsc_Socio,Dsc_Producto
ORDER BY ANIO, MES



SELECT ANIO, MES, Id_Socio, SOCIO, COUNT(TIENDA) AS TIENDAS, SUM(TRAMITES) AS TRAMITES  
FROM (
	SELECT YEAR(Fecha_Solicitud) AS ANIO, MONTH(Fecha_Solicitud) AS MES, A.Id_Socio
	, B.Dsc_Socio AS SOCIO, Dsc_Tienda AS TIENDA, COUNT(Case_Number) AS TRAMITES
	FROM Tabla_Captura_Rapida_DatosBasicos AS A
	INNER JOIN Cat_Socios AS B ON A.Id_Socio = B.Id_Socio 
		AND Fecha_Solicitud >= '2023-06-01 00:00:00' 
		AND Fecha_Solicitud < '2023-08-01 00:00:00'
		AND A.Id_Socio  IN('0')
	GROUP BY YEAR(Fecha_Solicitud), MONTH(Fecha_Solicitud),A.Id_Socio, B.Dsc_Socio,Dsc_Tienda 
) AS A
GROUP BY ANIO, MES, Id_Socio, SOCIO
ORDER BY ANIO, MES


SELECT ANIO, MES, Id_Socio, SOCIO, COUNT(PROMOTOR) AS PROMOTORES, SUM(TRAMITES) AS TRAMITES  
FROM (
	SELECT YEAR(Fecha_Solicitud) AS ANIO, MONTH(Fecha_Solicitud) AS MES, A.Id_Socio
	, B.Dsc_Socio AS SOCIO, Dsc_Promotor AS PROMOTOR, COUNT(Case_Number) AS TRAMITES
	FROM Tabla_Captura_Rapida_DatosBasicos AS A
	INNER JOIN Cat_Socios AS B ON A.Id_Socio = B.Id_Socio 
		AND Fecha_Solicitud >= '2023-06-01 00:00:00' 
		AND Fecha_Solicitud < '2023-10-10 00:00:00'
		AND A.Id_Socio  IN('0')
	GROUP BY YEAR(Fecha_Solicitud), MONTH(Fecha_Solicitud),A.Id_Socio, B.Dsc_Socio,Dsc_Promotor 
) AS A
GROUP BY ANIO, MES, Id_Socio, SOCIO
ORDER BY ANIO, MES
        