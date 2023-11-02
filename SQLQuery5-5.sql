-- Consulta para obtener los valores de Bines y NombreBin agrupados por idCampana
SELECT 
    idCampana,
    LEFT(noCuenta, 6) AS Bines,
    CASE 
        WHEN LEFT(noCuenta, 6) = '481284' THEN 'BK SUBURBIA'
        WHEN LEFT(noCuenta, 6) = '481281' THEN 'BK SHASA'
        WHEN LEFT(noCuenta, 6) = '403750' THEN 'BK PROMODA'
        WHEN LEFT(noCuenta, 6) = '464811' THEN 'BK LOB'
        WHEN LEFT(noCuenta, 6) = '481282' THEN 'BK GCC'
        WHEN LEFT(noCuenta, 6) = '446351' THEN 'BK C&A'
        WHEN LEFT(noCuenta, 6) = '469849' THEN 'BK BRADESCARD'
        WHEN LEFT(noCuenta, 6) = '481283' THEN 'BK BODEGA A.'
		WHEN LEFT(noCuenta,6)  = '506369' THEN 'PLCC SUBURBIA'
		WHEN LEFT(noCuenta, 6) = '506301' THEN  '  '
		WHEN LEFT(noCuenta, 6) = '506372' THEN 'PLCC SHASA'
		WHEN LEFT(noCuenta, 6) = '506469' THEN 'PLCC PROMODA'
		WHEN LEFT(noCuenta, 6) = '506370' THEN 'PLCC GCC'
		WHEN LEFT(noCuenta, 6) = '286900' THEN 'PLCC C&A'
		WHEN LEFT(noCuenta, 6) = '506329' THEN 'PLCC C&A'
        WHEN LEFT(noCuenta,6) = '506371' THEN 'PLCC BODEGA A.'
        WHEN LEFT(noCuenta, 6) = '286900' THEN 'PL/PP C&A'
        WHEN LEFT(noCuenta, 6) = '506330' THEN 'PL/PP C&A'
        WHEN LEFT(noCuenta, 6) = '506293' THEN 'PP BODEGA'
        WHEN LEFT(noCuenta, 6) = '506290' THEN 'PP SHASA'
        WHEN LEFT(noCuenta, 6) = '506360' THEN 'PP PROMODA'
        ELSE 'Otros'
    END AS NombreBin,
    COUNT(*) AS Cantidad
FROM tblCampanaEspecialAceptacion
WHERE 
    estatus = '1' AND
	fechaAceptacion >='2023-01-01' AND
	fechaAceptacion <= '2023-09-04'
GROUP BY idCampana, LEFT(noCuenta, 6)
ORDER BY idCampana;