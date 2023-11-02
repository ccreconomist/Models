SELECT 
    YEAR(Fecha_solicitud) AS Anio,
    MONTH(Fecha_solicitud) AS Mes,
    id_producto,
    Id_Socio,
    NUM_Scoring,
    COUNT(DISTINCT Dsc_Numero_Cuenta) AS CuentasUnicas,
    COUNT(DISTINCT Id_PreAprobado) AS IdPreaprobadosUnicos,
    CASE 
        WHEN id_producto = 1 THEN 'PLCC'
        WHEN id_producto = 2 THEN 'PLOAN'
        WHEN id_producto = 3 THEN 'BANK CARD'
        WHEN id_producto = 4 THEN 'TARJETA DE CREDITO'
        WHEN id_producto = 5 THEN 'PRESTAMO PERSONAL'
        WHEN id_producto = 7 THEN 'CDC'
        WHEN id_producto = 8 THEN 'PLCC LB'
        WHEN id_producto = 9 THEN 'BK LB'
        WHEN id_producto = 10 THEN 'PRESTAMO PERSONAL'
        WHEN id_producto = 11 THEN 'PRESTAMO PERSONAL'
        WHEN id_producto = 12 THEN 'PRESTAMO PERSONAL'
        ELSE 'Unknown'
    END AS Producto,
    CASE 
        WHEN Id_Socio = 0 THEN 'CyA'
        WHEN Id_Socio = 1 THEN 'BRADESCARD'
        WHEN Id_Socio = 2 THEN 'LOB'
        WHEN Id_Socio = 3 THEN 'SUBURBIA'
        WHEN Id_Socio = 4 THEN 'AURRERA'
        WHEN Id_Socio = 5 THEN 'SHASA'
        WHEN Id_Socio = 6 THEN 'GCC'
        WHEN Id_Socio = 7 THEN 'PROMODA'
        WHEN Id_Socio = 8 THEN 'CHEDRAUI'
        ELSE 'Unknown'
    END AS Socio
FROM 
    Tabla_PreAprobados
GROUP BY 
    YEAR(Fecha_solicitud), MONTH(Fecha_solicitud), id_producto, Id_Socio, NUM_Scoring,
    CASE 
        WHEN id_producto = 1 THEN 'PLCC'
        WHEN id_producto = 2 THEN 'PLOAN'
        WHEN id_producto = 3 THEN 'BANK CARD'
        WHEN id_producto = 4 THEN 'TARJETA DE CREDITO'
        WHEN id_producto = 5 THEN 'PRESTAMO PERSONAL'
        WHEN id_producto = 7 THEN 'CDC'
        WHEN id_producto = 8 THEN 'PLCC LB'
        WHEN id_producto = 9 THEN 'BK LB'
        WHEN id_producto = 10 THEN 'PRESTAMO PERSONAL'
        WHEN id_producto = 11 THEN 'PRESTAMO PERSONAL'
        WHEN id_producto = 12 THEN 'PRESTAMO PERSONAL'
        ELSE 'Unknown'
    END,
    CASE 
        WHEN Id_Socio = 0 THEN 'CyA'
        WHEN Id_Socio = 1 THEN 'BRADESCARD'
        WHEN Id_Socio = 2 THEN 'LOB'
        WHEN Id_Socio = 3 THEN 'SUBURBIA'
        WHEN Id_Socio = 4 THEN 'AURRERA'
        WHEN Id_Socio = 5 THEN 'SHASA'
        WHEN Id_Socio = 6 THEN 'GCC'
        WHEN Id_Socio = 7 THEN 'PROMODA'
        WHEN Id_Socio = 8 THEN 'CHEDRAUI'
        ELSE 'Unknown'
    END;

