SELECT 
    CUENTA, 
    ACTIVACION,
    MONTH(DATEADD(YEAR, 1, ACTIVACION)) AS Mes_Cumple_Anio,
    DATEADD(YEAR, 1, ACTIVACION) AS ANIVERSARIO
FROM IT_CARTERA_PLCC_EXT
WHERE DATEDIFF(YEAR, ACTIVACION, GETDATE()) = 1

UNION ALL

SELECT 
    CUENTA, 
    ACTIVACION,
    MONTH(DATEADD(YEAR, 1, ACTIVACION)) AS Mes_Cumple_Anio,
    DATEADD(YEAR, 1, ACTIVACION) AS ANIVERSARIO
FROM IT_CARTERA_BK
WHERE DATEDIFF(YEAR, ACTIVACION, GETDATE()) = 1

UNION ALL

SELECT 
    CUENTA, 
    ACTIVACION,
    MONTH(DATEADD(YEAR, 1, ACTIVACION)) AS Mes_Cumple_Anio,
    DATEADD(YEAR, 1, ACTIVACION) AS ANIVERSARIO
FROM IT_CARTERA_PL
WHERE DATEDIFF(YEAR, ACTIVACION, GETDATE()) = 1
ORDER BY Mes_Cumple_Anio, ANIVERSARIO;


