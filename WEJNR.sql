SELECT 
     NUM_CUENTA,
	 FECHA_CONSUMO,
	 FECHA_PROCESO,
	 TIPO_TRANSACCION,
	 RFC_COMERCIO,
	 IMP_DESTINO,
	 MCC_GIRO_COMERCIO
FROM PROSA_510
WHERE 
    FECHA_CONSUMO >= '2023-01-01 00:00:00.000' AND 
    FECHA_CONSUMO <= '2023-09-20 00:00:00.000' AND
    TIPO_TRANSACCION = '01' ;