SELECT
    PRODUCTO,
    COUNT(DISTINCT NUM_CUENTA) AS CONTEO_CUENTAS_UNICAS
FROM (
    -- Your original SELECT query here
    SELECT
        TARJETA,
        FECHA_NACIMIENTO,
        Bloq_Cobr,
        ESTADO,
        SEXO,
        CASE 
            WHEN SEXO = 1 THEN 'Masculino'
            WHEN SEXO = 2 THEN 'Femenino'
            ELSE ''
        END AS GENERO,
        EDO_CIVIL,
        DATEDIFF(YEAR, FECHA_NACIMIENTO, GETDATE()) AS EDAD,
        ULTC,
        CUENTA,
        LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) AS BINES,
        SUBSTRING(CUENTA, 4, LEN(CUENTA)) AS NUM_CUENTA,
        CASE 
            WHEN BLOQ_OPER = '' THEN ''
            ELSE 'Q'
        END AS BLOQ_OPER,
        CASE
            WHEN Bloq_Cobr = 'G' THEN 'COB PREVENTIVA'
            WHEN Bloq_Cobr = 'N' THEN 'ACUERDO c/n Pago Inicial'
            WHEN Bloq_Cobr = 'U' THEN 'ATRASO de 120 a 179 días'
            WHEN Bloq_Cobr = 'W' THEN 'ATRASO de 1 a 8 días'
            WHEN Bloq_Cobr = 'X' THEN 'ATRASO de 9 a 59 días'
            WHEN Bloq_Cobr = 'Y' THEN 'ATRASO de 60 a 119 días'
            WHEN Bloq_Cobr = 'Z' THEN 'ACUERDO PENDIENTE Sin Pago Inicial'
            WHEN Bloq_Cobr = '' THEN ''
            ELSE ''
        END AS BLOQ_COBR_ETIQUETA,
        CASE
            WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '286900' THEN 'C&A'
            WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '506329' THEN 'G&A'
			WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '481282' THEN 'C&A'
            ELSE ''
        END AS SOCIO,
        CASE
            WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '286900' THEN 'PLCC'
			WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '506329' THEN 'PLCC'
            WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '446351' THEN 'BK'
            ELSE ''
        END AS PRODUCTO
    FROM
        IT_CARTERA_PLCC_EXT
    WHERE
        LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) IN ('286900','506329', '446351')
) AS UniqueAccountsCount
GROUP BY PRODUCTO;


