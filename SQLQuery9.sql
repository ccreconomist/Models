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
        WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '506469' THEN 'PROMODA'
        ELSE ''
    END AS SOCIO,
    CASE
        WHEN LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) = '403750' THEN 'BK'
        ELSE ''
    END AS PRODUCTO
FROM
    IT_CARTERA_SHASA
WHERE
    LEFT(REPLACE(SUBSTRING(CUENTA, 4, LEN(CUENTA)), '000', ''), 6) IN ('481281', '506372');
