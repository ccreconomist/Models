SELECT ANIO, MES, Id_Socio, SOCIO, COUNT(Case_Number) AS TRAMITES, PRODUCTO
FROM(
	SELECT DISTINCT YEAR(Fecha_Solicitud) AS ANIO, MONTH(Fecha_Solicitud) AS MES, Id_Socio
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
	WHERE Fecha_Solicitud >= '2023-08-01 00:00:00' 
		AND Fecha_Solicitud < '2023-08-31   00:00:00'
		AND Id_Socio IN (0,4,5,6,7)
		AND Num_Tienda NOT IN ('899')
		----AND AnalistaCaptura NOT LIKE '%Usronline%'
) AS A
GROUP BY ANIO, MES, Id_Socio, SOCIO, PRODUCTO
ORDER BY ANIO, MES, Id_Socio