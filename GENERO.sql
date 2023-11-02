SELECT
    PRODUCTO,
    GENERO,
    CASE
        WHEN EDAD BETWEEN 18 AND 24 THEN '18-24'
        WHEN EDAD BETWEEN 25 AND 34 THEN '25-34'
        WHEN EDAD BETWEEN 35 AND 44 THEN '35-44'
        WHEN EDAD BETWEEN 45 AND 54 THEN '45-54'
        WHEN EDAD BETWEEN 55 AND 64 THEN '55-64'
        WHEN EDAD >= 65 THEN '65+'
        ELSE 'Unknown'
    END AS RANGO_EDAD,
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
            WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '506469' THEN 'C&A'
            --WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '506329' THEN 'G&A'
            WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '403750' THEN 'C&A'
            ELSE ''
        END AS SOCIO,
        CASE
            WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '506469' THEN 'PLCC'
            --WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '506329' THEN 'PLCC'
            WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '403750' THEN 'BK'
            ELSE ''
        END AS PRODUCTO
    FROM
        IT_CARTERA_B
    WHERE
        LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) IN ('506469', '403750')
) AS UniqueAccountsCount
GROUP BY PRODUCTO, GENERO,
         CASE
            WHEN EDAD BETWEEN 18 AND 24 THEN '18-24'
            WHEN EDAD BETWEEN 25 AND 34 THEN '25-34'
            WHEN EDAD BETWEEN 35 AND 44 THEN '35-44'
            WHEN EDAD BETWEEN 45 AND 54 THEN '45-54'
            WHEN EDAD BETWEEN 55 AND 64 THEN '55-64'
            WHEN EDAD >= 65 THEN '65+'
            ELSE 'Unknown'
        END;
