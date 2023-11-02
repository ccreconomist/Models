WITH PeriodoActual AS (
    SELECT 
        FECHA_CONSUMO AS Fecha,
        NUM_CUENTA,
        IMP_DESTINO
    FROM PROSA_510
    WHERE 
        FECHA_CONSUMO >= '2023-07-01 00:00:00.000' AND 
        FECHA_CONSUMO <= '2023-08-28 00:00:00.000' AND 
        TIPO_TRANSACCION = '01' AND 
        LEFT(NUM_CUENTA, 6) IN ('481284','481281', '403750', '481282', '446351', '481283')

),
Metrics AS (
    SELECT
        PA.Fecha,
        COUNT(*) AS Total_Transacciones,
        COUNT(DISTINCT PA.NUM_CUENTA) AS Total_Cuentas_Unicas,
        SUM(PA.IMP_DESTINO) AS Suma_Importes
    FROM PeriodoActual PA
    GROUP BY PA.Fecha
)
SELECT
    M.Fecha,
    M.Total_Transacciones,
    M.Total_Cuentas_Unicas,
    M.Suma_Importes,
    M.Total_Transacciones - COALESCE(M_Prev.Total_Transacciones, 0) AS Incremento_Transacciones,
    M.Total_Cuentas_Unicas - COALESCE(M_Prev.Total_Cuentas_Unicas, 0) AS Incremento_Cuentas_Unicas,
    M.Suma_Importes - COALESCE(M_Prev.Suma_Importes, 0) AS Incremento_Importes
FROM Metrics M
LEFT JOIN Metrics M_Prev ON M.Fecha - 1 = M_Prev.Fecha
ORDER BY M.Fecha;

