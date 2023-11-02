SELECT DISTINCT Nombre_Tienda,
    Id_Socio,
    Status1,
    Fecha_Solicitud,
    Fecha_Corte,
    Fecha_Pago,
    Fecha_activacion_cuenta1,
    No_Solicitud,
    Case_Number,
    Dsc_Numero_Cuenta1,
    RIGHT(CONVERT(VARCHAR, Fecha_Corte, 12), 2) AS Corte,
    CASE
        WHEN Id_Socio = 0 THEN 'C&A'
        WHEN Id_Socio = 1 THEN 'BRADESCARD'
        WHEN Id_Socio = 2 THEN 'LOB'
        WHEN Id_Socio = 3 THEN 'SUBURBIA'
        WHEN Id_Socio = 4 THEN 'BODEGA'
        WHEN Id_Socio = 5 THEN 'SHASA'
        WHEN Id_Socio = 6 THEN 'GCC'
        WHEN Id_Socio = 7 THEN 'PROMODA' 
        ELSE 'OTRO'
    END AS SOCIO,
    Num_Tienda
FROM V_Datos_Generales
WHERE Status1 = 'APROBADO'
    AND Fecha_Solicitud >= '2023-10-01'
    AND Fecha_Solicitud < GETDATE()
	AND Id_Socio <> 0
	AND Fecha_activacion_cuenta1 <> 'NULL'
    AND NOT (
        (Id_Socio = 4 AND Num_Tienda IN (12, 55, 59, 63, 72, 79, 90, 119, 120, 133, 144, 151, 152, 160, 215, 232, 251, 265, 271, 272, 275, 276, 292, 293, 307, 312, 319, 328, 340, 347, 348))
         OR (Id_Socio = 6 AND Num_Tienda IN (109, 115, 152, 161, 162, 163, 169, 171, 173, 192, 212, 251, 275))
         OR (Id_Socio = 7 AND Num_Tienda IN (5, 13, 17, 44, 156, 213, 225, 231, 250))
         OR (Id_Socio = 5 AND Num_Tienda IN (61,78,83,115,117))
    )
ORDER BY SOCIO, Num_Tienda, Corte
