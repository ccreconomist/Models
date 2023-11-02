SELECT 
    noCuenta,
	idCampana,
	fechaAceptacion,
	estatus
FROM tblCampanaEspecialAceptacion
 WHERE
        idCampana = '182'
        AND estatus = '1';
