SELECT FECHA, Id_Socio, SOCIO, COUNT(Case_Number) AS TRAMITES, PRODUCTO
FROM(
	SELECT DISTINCT Fecha_Solicitud AS FECHA, Id_Socio
	, CASE	WHEN Id_Socio = 0 THEN 'C&A'
				WHEN Id_Socio = 1 THEN 'BRADESCARD'
				WHEN Id_Socio = 2 THEN 'LOB'
				WHEN Id_Socio = 3 THEN 'SUBURBIA'
				WHEN Id_Socio = 4 THEN 'BODEGA'
				WHEN Id_Socio = 5 THEN 'SHASA'
				WHEN Id_Socio = 6 THEN 'GCC'
				WHEN Id_Socio = 7 THEN 'PROMODA' 
			ELSE 'OTRO' END SOCIO
		, Case_Number  --COUNT(Case_Number) AS TRAMITES
		, CASE	WHEN Dsc_Producto LIKE 'B%' THEN 'BK'
				WHEN Dsc_Producto LIKE 'PLCC %' THEN 'PLCC'
				WHEN Dsc_Producto LIKE 'PRESTAMO%' THEN 'PL'
				WHEN Dsc_Producto = 'PLOAN' THEN 'PL' ELSE Dsc_Producto END AS PRODUCTO
	FROM V_Datos_Generales
	WHERE Fecha_Solicitud >= '2023-01-01 00:00:00' 
		AND Fecha_Solicitud < '2023-10-12 00:00:00'
		AND Id_Socio IN (0,4,5,6,7)
		AND Num_Tienda NOT IN ('899')
		AND AnalistaCaptura NOT LIKE '%Usronline%'
) AS A
GROUP BY FECHA, Id_Socio, SOCIO, PRODUCTO
ORDER BY FECHA, Id_Socio

/*
 --- por tienda

SELECT YEAR(Fecha_Solicitud) AS ANIO, MONTH(Fecha_Solicitud) AS MES, Id_Socio
, CASE	WHEN Id_Socio = 0 THEN 'C&A'
			WHEN Id_Socio = 1 THEN 'BRADESCARD'
			WHEN Id_Socio = 2 THEN 'LOB'
			WHEN Id_Socio = 3 THEN 'SUBURBIA'
			WHEN Id_Socio = 4 THEN 'BODEGA'
			WHEN Id_Socio = 5 THEN 'SHASA'
			WHEN Id_Socio = 6 THEN 'GCC'
			WHEN Id_Socio = 7 THEN 'PROMODA' 
		ELSE 'OTRO' END SOCIO
	,  COUNT(Case_Number) AS TRAMITES--, Dsc_Producto
	, Num_Tienda AS TIENDA
FROM V_Datos_Generales
WHERE Fecha_Solicitud >= '2019-01-01 00:00:00' 
	AND Fecha_Solicitud < '2021-11<1-01 00:00:00'
	AND Id_Socio IN (7)
	AND Num_Tienda NOT IN ('899')
	AND AnalistaCaptura != 'UsronlineProm'
GROUP BY YEAR(Fecha_Solicitud), MONTH(Fecha_Solicitud),  Id_Socio, Dsc_Socio, Num_Tienda 
ORDER BY ANIO, MES, TIENDA

*/


SELECT FECHA, Id_Socio, SOCIO, COUNT(TIENDA) AS TIENDAS, SUM(TRAMITES) AS TRAMITES  
FROM (
	SELECT FECHA, Id_Socio, SOCIO, TIENDA, COUNT(Case_Number) AS TRAMITES 
	FROM ( 
		SELECT DISTINCT Fecha_Solicitud AS FECHA, Id_Socio
		, CASE	WHEN Id_Socio = 0 THEN 'C&A'
					WHEN Id_Socio = 1 THEN 'BRADESCARD'
					WHEN Id_Socio = 2 THEN 'LOB'
					WHEN Id_Socio = 3 THEN 'SUBURBIA'
					WHEN Id_Socio = 4 THEN 'BODEGA'
					WHEN Id_Socio = 5 THEN 'SHASA'
					WHEN Id_Socio = 6 THEN 'GCC'
					WHEN Id_Socio = 7 THEN 'PROMODA' 
				ELSE 'OTRO' END SOCIO
			, Num_Tienda AS TIENDA, Case_Number --COUNT(Case_Number) AS TRAMITES
		FROM V_Datos_Generales
		WHERE Fecha_Solicitud >= '2023-01-01 00:00:00' 
		AND Fecha_Solicitud < '2023-10-12 00:00:00'
			AND Id_Socio IN (0,4,5,6,7)
			--AND AnalistaCaptura != 'UsronlineProm'
			AND AnalistaCaptura NOT LIKE '%Usronline%'
	) AS A
	GROUP BY  FECHA, Id_Socio, SOCIO, TIENDA
) AS A
GROUP BY  FECHA, Id_Socio, SOCIO
ORDER BY  FECHA, Id_Socio



SELECT FECHA, Id_Socio, SOCIO, COUNT(PROMOTOR) AS PROMOTORES, SUM(TRAMITES) AS TRAMITES  
FROM (
	SELECT FECHA, Id_Socio, SOCIO, PROMOTOR, COUNT(Case_Number) AS TRAMITES 
	FROM (
		SELECT DISTINCT Fecha_Solicitud AS FECHA, MONTH(Fecha_Solicitud) AS MES, Id_Socio
		, CASE	WHEN Id_Socio = 0 THEN 'C&A'
					WHEN Id_Socio = 1 THEN 'BRADESCARD'
					WHEN Id_Socio = 2 THEN 'LOB'
					WHEN Id_Socio = 3 THEN 'SUBURBIA'
					WHEN Id_Socio = 4 THEN 'BODEGA'
					WHEN Id_Socio = 5 THEN 'SHASA'
					WHEN Id_Socio = 6 THEN 'GCC'
					WHEN Id_Socio = 7 THEN 'PROMODA' 
				ELSE 'OTRO' END SOCIO
			, Num_Promotor AS PROMOTOR, Case_Number-- COUNT(Case_Number) AS TRAMITES
		FROM V_Datos_Generales
		WHERE Fecha_Solicitud >= '2023-01-01 00:00:00' 
		AND Fecha_Solicitud < '2023-10-12 00:00:00'
			AND Id_Socio IN (0,4,5,6,7)
			--AND AnalistaCaptura != 'UsronlineProm'
			AND AnalistaCaptura NOT LIKE '%Usronline%'
	) AS A
	GROUP BY  FECHA, Id_Socio, SOCIO, PROMOTOR
) AS A
GROUP BY  FECHA, Id_Socio, SOCIO
ORDER BY  FECHA, Id_Socio
