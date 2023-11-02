SELECT CAST(Fecha_Solicitud AS DATE) AS FECHA
	, CASE  WHEN Id_Socio = 0 THEN 'C&A'
			WHEN Id_Socio = 1 THEN 'BRADESCARD'
			WHEN Id_Socio = 2 THEN 'LOB'
			WHEN Id_Socio = 3 THEN 'SUBURBIA'
			WHEN Id_Socio = 4 THEN 'BODEGA'
			WHEN Id_Socio = 5 THEN 'SHASA'
			WHEN Id_Socio = 6 THEN 'GCC'
			WHEN Id_Socio = 7 THEN 'PROMODA'
		Else 'OTRO' END SOCIO
	, COUNT(Case_Number) AS TRAMITES
	, CASE  WHEN Dsc_Producto IS NULL THEN 'PLCC'
			WHEN Dsc_Producto = 'PLOAN' THEN 'PP'
			WHEN Dsc_Producto = 'BANK CARD' THEN 'BK_PRE'
	Else 'PLCC' END AS PRODUCTO
FROM V_Producto
WHERE CAST(Fecha_Solicitud AS DATE) >= '2023-01-01' AND CAST(Fecha_Solicitud AS DATE)  <= CAST('2023-10-15' AS DATE) AND Id_Socio = 0
GROUP BY CAST(Fecha_Solicitud AS DATE)
	, CASE  WHEN Id_Socio = 0 THEN 'C&A'
			WHEN Id_Socio = 1 THEN 'BRADESCARD'
			WHEN Id_Socio = 2 THEN 'LOB'
			WHEN Id_Socio = 3 THEN 'SUBURBIA'
			WHEN Id_Socio = 4 THEN 'BODEGA'
			WHEN Id_Socio = 5 THEN 'SHASA'
			WHEN Id_Socio = 6 THEN 'GCC'
			WHEN Id_Socio = 7 THEN 'PROMODA'
		Else 'OTRO' END
	, CASE  WHEN Dsc_Producto IS NULL THEN 'PLCC'
			WHEN Dsc_Producto = 'PLOAN' THEN 'PP'
			WHEN Dsc_Producto = 'BANK CARD' THEN 'BK_PRE'
	Else 'PLCC' END