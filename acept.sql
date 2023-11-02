SELECT 
    idAceptacion,
    noCliente,
    noCuenta,
    idCampana,
    nombreCampana,
    estatus,
    fechaAceptacion,
    LEFT(noCuenta, 6) AS noCuenta2,
    SUBSTRING(CONVERT(VARCHAR(255), noCuenta), 1, LEN(CONVERT(VARCHAR(255), noCuenta)) - 3) + '000' AS CUENTA
FROM tblCampanaEspecialAceptacion
WHERE 
    idCampana = '167'
    AND fechaAceptacion >= '2023-07-17 00:00:00.000'
    AND fechaAceptacion <= '2023-08-07 00:00:00.000'
    AND estatus = '1'
    AND LEFT(noCuenta, 6) IN ('481284', '481281', '403750', '481282', '446351', '481283');
