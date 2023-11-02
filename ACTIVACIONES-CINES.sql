SELECT 

    idAceptacion,

    noCliente,

    noCuenta,

    idCampana,

    estatus,

    fechaAceptacion,

    LEFT(noCuenta, 6) AS noCuenta2,

    SUBSTRING(CONVERT(VARCHAR(255), noCuenta), 1, LEN(CONVERT(VARCHAR(255), noCuenta)) - 3) + '000' AS CUENTA

FROM tblCampanaEspecialAceptacion

WHERE 

    idCampana = '190'
	
    --AND fechaAceptacion >= '2023-09-28 00:00:00.000'
    
	--AND fechaAceptacion <= '2023-09-29 00:00:00.000'

    AND estatus = '1'

	AND LEFT(noCuenta, 6) IN ('481284', '481281', '403750', '464811', '481282', '446351', '481283', '469849');