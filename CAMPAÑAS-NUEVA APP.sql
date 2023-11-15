SELECT
    *,
    '000' + SUBSTRING(numero_tarjeta_campana, 1, LEN(numero_tarjeta_campana) - 3) + '000' AS CUENTA
FROM viw_actividad_campanas
WHERE 
    id_magnolia = '2315CEGCCCP' --gcc
    AND tipo_evento = 'suscrito';
