SELECT
    PRODUCTO,
    NO_DE_CUENTA,
    NUM_CUENTA,
    RFC_COMERCIO,
    FECHA_CONSUMO,
    COUNT(DISTINCT NUM_CUENTA) AS NUM_CUENTAS_UNICAS,
    COUNT(IMP_DESTINO) AS TXN,
    SUM(IMP_DESTINO) AS MONTO_IMP_DESTINO_POR_DIA
FROM (
    SELECT
        CASE 
            WHEN LEFT(NUM_CUENTA, 6) = '506369' THEN 'PLCC SUBURBIA'
            WHEN LEFT(NUM_CUENTA, 6) = '506372' THEN 'PLCC SHASA'
            WHEN LEFT(NUM_CUENTA, 6) = '506469' THEN 'PLCC PROMODA'
            WHEN LEFT(NUM_CUENTA, 6) = '506370' THEN 'PLCC GCC'
            WHEN LEFT(NUM_CUENTA, 6) = '286900' THEN 'PLCC C&A'
            WHEN LEFT(NUM_CUENTA, 6) = '506329' THEN 'PLCC C&A'
            WHEN LEFT(NUM_CUENTA, 6) = '506370' THEN 'PLCC BODEGA A'
            WHEN LEFT(NUM_CUENTA, 6) = '481284' THEN 'BK SUBURBIA'
            WHEN LEFT(NUM_CUENTA, 6) = '481281' THEN 'BK SHASA'
            WHEN LEFT(NUM_CUENTA, 6) = '403750' THEN 'BK PROMODA'
            WHEN LEFT(NUM_CUENTA, 6) = '464811' THEN 'BK LOB'
            WHEN LEFT(NUM_CUENTA, 6) = '481282' THEN 'BK GCC'
            WHEN LEFT(NUM_CUENTA, 6) = '446351' THEN 'BK C&A'
            WHEN LEFT(NUM_CUENTA, 6) = '469849' THEN 'BK BRADESCARD'
            WHEN LEFT(NUM_CUENTA, 6) = '481283' THEN 'BK BODEGA'
            WHEN LEFT(NUM_CUENTA, 6) = '286900' THEN 'PP/PL C&A'
            WHEN LEFT(NUM_CUENTA, 6) = '506330' THEN 'PP/PL C&A'
            WHEN LEFT(NUM_CUENTA, 6) = '506293' THEN 'PP/PL BODEGA'
            WHEN LEFT(NUM_CUENTA, 6) = '506290' THEN 'PP/PL SHASA'
            WHEN LEFT(NUM_CUENTA, 6) = '506360' THEN 'PP/PL PROMODA'
            ELSE 'Other'
        END AS PRODUCTO,
        LEFT(NUM_CUENTA, 6) AS NO_DE_CUENTA,
        NUM_CUENTA,
        RFC_COMERCIO,
        FECHA_CONSUMO,
        IMP_DESTINO
    FROM PROSA_510
    WHERE FECHA_CONSUMO >= '2023-01-01 00:00:00.000' AND 
          FECHA_CONSUMO <= '2023-10-03 00:00:00.000' AND 
          TIPO_TRANSACCION = '01'
) AS SubQueryAlias
GROUP BY PRODUCTO, NO_DE_CUENTA, NUM_CUENTA, RFC_COMERCIO, FECHA_CONSUMO
ORDER BY FECHA_CONSUMO, RFC_COMERCIO;