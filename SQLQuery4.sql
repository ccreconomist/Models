SELECT *
FROM tblCampanaEspecialAceptacion
WHERE 
	 idCampana = '180'
	 AND fechaAceptacion >= '2023-08-25 00:00:00.000'
	 AND fechaAceptacion <= '2023-08-29 00:00:00.000'   
	 AND estatus = '1';