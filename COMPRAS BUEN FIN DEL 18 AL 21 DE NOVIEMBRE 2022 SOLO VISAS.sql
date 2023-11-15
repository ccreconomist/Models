SELECT 
    NUM_CUENTA,
    COUNT(NUM_AUT) AS Transacciones,
    SUM(IMP_DESTINO) AS Facturacion,
    '000' + SUBSTRING(CONVERT(VARCHAR(50), NUM_CUENTA), 1, LEN(NUM_CUENTA) - 3) + '000' AS CUENTA
FROM PROSA_510
WHERE 
    FECHA_CONSUMO >= '2022-11-17 00:00:00.000' AND 
    FECHA_CONSUMO <= '2022-11-22 00:00:00.000' AND
    TIPO_TRANSACCION = '01' AND
    LEFT(NUM_CUENTA, 6) IN ('481284', '481281', '403750', '464811', '481282', '446351', '481283')
GROUP BY NUM_CUENTA
--HAVING SUM(IMP_DESTINO) < 3000;