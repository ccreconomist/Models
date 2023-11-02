WITH CuentasUnicasPorCampana AS (
    SELECT 
        idCampana,
        fechaAceptacion,
        COUNT(DISTINCT noCliente) AS cuentasUnicas
    FROM tblCampanaEspecialAceptacion
    WHERE 
        fechaAceptacion >= '2023-01-01 00:00:00.000'
        AND fechaAceptacion <= '2023-08-31 00:00:00.000'
        AND estatus = '1'
    GROUP BY 
        idCampana,
        fechaAceptacion
)
SELECT
    idCampana,
    SUM(cuentasUnicas) AS cuentasUnicasPorCampana
FROM CuentasUnicasPorCampana
GROUP BY idCampana;

