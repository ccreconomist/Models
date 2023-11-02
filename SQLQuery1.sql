SELECT
    TARJETA,
    FECHA_NACIMIENTO,
    Bloq_Cobr,
    SEXO,
    CASE 
        WHEN SEXO = 1 THEN 'Masculino'
        WHEN SEXO = 2 THEN 'Femenino'
        ELSE ''
    END AS GENERO,
    EDO_CIVIL,
    ULTC,
    ULTC,
    ULTP,
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
        WHEN Bloq_Cobr = '' THEN '' -- Mantener vacío si Bloq_Cobr está vacío
        ELSE ''
    END AS BLOQ_COBR_ETIQUETA,
    CASE
        WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '286900' THEN 'C&A' --CAMBIAR
        WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '506329' THEN 'C&A' --CAMBIAR
        ELSE ''
    END AS SOCIO,
    CASE
        WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '506329' THEN 'PLCC' --CAMBIAR
        WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '286900' THEN 'PLCC'---CAMBIAR
        ELSE ''
    END AS PRODUCTO,
    CASE
        WHEN ULTC IS NULL THEN 'NUNCA ACTIVO'
        WHEN ULTC >= DATEADD(DAY, -30, GETDATE()) THEN 'ACTIVE'
        WHEN ULTC BETWEEN DATEADD(DAY, -365, GETDATE()) AND DATEADD(DAY, -31, GETDATE()) THEN 'INACTIVE'
        ELSE 'CUENTAS DORMIDAS'
    END AS TIPO
FROM
    IT_CARTERA_PLCC_EXT
WHERE
    LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) IN ('286900', '506329'); --CAMBIAR

