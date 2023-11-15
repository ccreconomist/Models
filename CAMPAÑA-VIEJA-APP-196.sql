SELECT
    *,
    '000' + SUBSTRING(CONVERT(VARCHAR(50), noCuenta), 1, LEN(noCuenta) - 3) + '000' AS CUENTA
FROM tblCampanaEspecialAceptacion
WHERE 
    idCampana = '196'
    --AND fechaAceptacion >= '2023-08-25 00:00:00.000'
    --AND fechaAceptacion <= '2023-08-29 00:00:00.000'   
    AND estatus = '1';
