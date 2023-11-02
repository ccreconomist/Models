WITH PeriodoActual AS (
    SELECT 
        DAY(FECHA_CONSUMO) AS Dia_Mes,
        MIN(FECHA_CONSUMO) AS Fecha_Inicio,
        MAX(FECHA_CONSUMO) AS Fecha_Fin,
        COUNT(*) AS Total_Transacciones,
        COUNT(DISTINCT NUM_CUENTA) AS Total_Cuentas_Unicas,
        SUM(IMP_DESTINO) AS Suma_Importes
    FROM PROSA_510
    WHERE 
        FECHA_CONSUMO >= '2023-01-01 00:00:00.000' AND 
        FECHA_CONSUMO <= '2023-08-28 00:00:00.000' AND 
        TIPO_TRANSACCION = '01' AND 
        LEFT(NUM_CUENTA, 6) IN ('481284', '481281', '403750', '464811', '481282', '446351', '469849', '481283')
    GROUP BY DAY(FECHA_CONSUMO)
)
SELECT
    PA.Dia_Mes,
    PA.Fecha_Inicio,
    PA.Fecha_Fin,
    PA.Total_Transacciones,
    PA.Total_Cuentas_Unicas,
    PA.Suma_Importes,
    PA.Total_Transacciones - COALESCE(PA_Prev.Total_Transacciones, 0) AS Incremento_Transacciones,
    PA.Total_Cuentas_Unicas - COALESCE(PA_Prev.Total_Cuentas_Unicas, 0) AS Incremento_Cuentas_Unicas,
    PA.Suma_Importes - COALESCE(PA_Prev.Suma_Importes, 0) AS Incremento_Importes
FROM PeriodoActual PA
LEFT JOIN PeriodoActual PA_Prev ON PA.Dia_Mes - 1 = PA_Prev.Dia_Mes
ORDER BY PA.Dia_Mes;
