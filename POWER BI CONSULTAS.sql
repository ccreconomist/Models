WITH comercio_mapping AS (
    SELECT 
        RFC_COMERCIO,
        CASE
        WHEN NOMBRE_COMERCIO LIKE'%UBER%EATS%' THEN 'UBER EATS' 
WHEN NOMBRE_COMERCIO LIKE '%SPOTIFY%' THEN 'SPOTIFY'
WHEN NOMBRE_COMERCIO LIKE '%GOOGLE%' THEN 'GOOGLE'
WHEN NOMBRE_COMERCIO LIKE '%AIRBNB%' THEN 'AIRBNB'
WHEN NOMBRE_COMERCIO LIKE '%FACEBK%' THEN 'FACEBOOK'
WHEN NOMBRE_COMERCIO ='PLAYSTATION NETWORK' THEN 'PlaystationNetwork'
WHEN RFC_COMERCIO = 'TSP 0004051I4' THEN 'NETO'
WHEN RFC_COMERCIO = 'MSK 181210PN0' THEN 'SKX'
WHEN RFC_COMERCIO = 'TCA 0407219T6' THEN 'MEGACABLE'
WHEN RFC_COMERCIO = 'MME 910620Q85' THEN 'MICROSOFT'
WHEN RFC_COMERCIO = 'CSS 160330CP7' THEN 'CFE'
WHEN RFC_COMERCIO = 'TME 840315KT6' THEN 'TELMEX'
WHEN RFC_COMERCIO = 'PPC 980624U16' THEN 'TELEFONICA'
WHEN RFC_COMERCIO = 'CON 101129UK0' THEN 'SR PAGO*SENOR PAGO'
WHEN RFC_COMERCIO = 'TBR 080613EN5' THEN 'TERRAMAR BRANDS'
WHEN RFC_COMERCIO = 'GCA 951222FA5' THEN 'CALZZAPATO'
WHEN RFC_COMERCIO = 'HAM 111006K69' THEN 'H&M'
WHEN RFC_COMERCIO = 'PPL 961114GZ1' THEN 'FARMACIAS SAN PABLO'
WHEN RFC_COMERCIO = 'PHI 830429MG6' THEN 'EL PALACIO DE HIERRO'
WHEN RFC_COMERCIO = 'JTI 950613GS8' THEN 'JARDINES DEL TIEMPO'
WHEN RFC_COMERCIO = 'YRM 911028F3A' THEN 'YVES ROCHER'
WHEN RFC_COMERCIO = 'SME 970819KD6' THEN 'SWISS JUST'
WHEN RFC_COMERCIO = 'SCG 820209HP4' THEN 'SERVICIO COMERCIAL GARIS'
WHEN RFC_COMERCIO = 'SCD 031029LXA' THEN 'SUPERBOLETOS'
WHEN RFC_COMERCIO = 'EIS 430714ER6' THEN 'UNIV TEC MILENIO'
WHEN RFC_COMERCIO = 'SOM 101125UEA' THEN 'SEARS'
WHEN RFC_COMERCIO = 'CGA 160215952' THEN 'COSTCO GAS'
WHEN RFC_COMERCIO = 'PAR 900605CAA' THEN 'LA GRAN BODEGA'
WHEN RFC_COMERCIO = 'TSC 1503258J2' THEN 'GRABASA - TYPHOON SPORTS'
WHEN RFC_COMERCIO = 'DME 130805134' THEN 'DO TERRA'
WHEN RFC_COMERCIO = 'SHE 190630V37' THEN 'SANBORNS'
WHEN RFC_COMERCIO = 'EAI 991209TV8' THEN 'FONICE TELEMARKETING'
WHEN RFC_COMERCIO = 'QCS 931209G49' THEN 'QUALITAS'
WHEN RFC_COMERCIO = 'TAA 060329410' THEN 'TIENDA AMIGA'
WHEN RFC_COMERCIO = 'AEB 611030SN7' THEN 'AUTOBUSES ESTRELLA BLANCA'
WHEN RFC_COMERCIO = 'AME 880912I89' THEN 'AEROMEXICO'
WHEN RFC_COMERCIO = 'HBA 930609L84' THEN 'ZAPATERIAS B HERMANOS'
WHEN RFC_COMERCIO = 'CSD 161207R2A' THEN 'SODIMAC'
WHEN RFC_COMERCIO = 'NMP 7502257ZA' THEN 'NACIONAL MONTE DE PIEDAD'
WHEN RFC_COMERCIO = 'RME 140210IY5' THEN 'LEFTIES'
WHEN RFC_COMERCIO = 'MAS 121116E51' THEN 'PETCO'
WHEN RFC_COMERCIO = 'UTM 7502128J2' THEN 'UNITEC'
WHEN RFC_COMERCIO = 'GNP 9211244P0' THEN 'GNP'
WHEN RFC_COMERCIO = 'BOD 9809059Z6' THEN 'LA MARINA'
WHEN RFC_COMERCIO = 'EME 041008RM2' THEN 'EXPEDIA - HOTELES.COM'
WHEN RFC_COMERCIO = 'HIM 890120VEA' THEN 'HERBALIFE'
WHEN RFC_COMERCIO = 'SIN 9408027L7' THEN 'SEGUROS INB'
WHEN RFC_COMERCIO = 'GZA 9104307K6' THEN 'ZORRO'
WHEN RFC_COMERCIO = 'SMN 930802FN9' THEN 'SEGUROS MONTERREY NY LIFE'
WHEN RFC_COMERCIO = 'MME 920427EM3' THEN 'METLIFE'
WHEN RFC_COMERCIO = 'FVM 120229UY6' THEN 'FOREVER 21'
WHEN RFC_COMERCIO = 'NME 920220KL4' THEN 'NIKE FACTORY'
WHEN RFC_COMERCIO = 'MLS 020424LM2' THEN 'MONTEPIO'
WHEN RFC_COMERCIO = 'SGM 950714DC2' THEN 'OXXO GAS'
WHEN RFC_COMERCIO = 'AAE 050309FM0' THEN 'INTERJET'
WHEN RFC_COMERCIO = 'AME 970109GW0' THEN 'AUTOZONE'
WHEN RFC_COMERCIO = 'ANA 050518RL1' THEN 'VIVA AEROBUS'
WHEN RFC_COMERCIO = 'AOR 540203NL7' THEN 'ADO'
WHEN RFC_COMERCIO = 'AOZ 9903024A5' THEN 'OZONO'
WHEN RFC_COMERCIO = 'API 6609273E0' THEN 'GRUPO FLECHA AMARILLA'
WHEN RFC_COMERCIO = 'BBS 070606D33' THEN 'BEST BUY'
WHEN RFC_COMERCIO = 'BME 0004112J6' THEN 'BERSHKA'
WHEN RFC_COMERCIO = 'BME 010405MX7' THEN 'TODO MODA'
WHEN RFC_COMERCIO = 'CAG 0412176A6' THEN 'CUIDADO CON EL PERRO'
WHEN RFC_COMERCIO = 'CCO 8605231N4' THEN 'OXXO'
WHEN RFC_COMERCIO = 'CFC 110121742' THEN 'FARMACIA DEL AHORRO'
WHEN RFC_COMERCIO = 'CLE 810525EA1' THEN 'LEY'
WHEN RFC_COMERCIO = 'CME 910715UB9' THEN 'COSTCO'
WHEN RFC_COMERCIO = 'CNO 960830IT7' THEN 'CA SKY'
WHEN RFC_COMERCIO = 'COP 920428Q20' THEN 'COPPEL'
WHEN RFC_COMERCIO = 'CSI 020226MV4' THEN 'STARBUCKS'
WHEN RFC_COMERCIO = 'CVA 041027H80' THEN 'VOLARIS'
WHEN RFC_COMERCIO = 'DJU 890724BU0' THEN 'JUGUETRON'
WHEN RFC_COMERCIO = 'DMA 850716ER5' THEN 'DEPORTES MARTI'
WHEN RFC_COMERCIO = 'FBE 9110215Z3' THEN 'FARMACIAS BENAVIDES'
WHEN RFC_COMERCIO = 'FCA 980701L75' THEN 'CALZADO ANDREA'
WHEN RFC_COMERCIO = 'FGU 830930PD3' THEN 'FARMACIAS GUADALAJARA'
WHEN RFC_COMERCIO = 'GAM 0309104A4' THEN 'GAME PLANET'
WHEN RFC_COMERCIO = 'GES 021031BL9' THEN 'PRICE SHOES'
WHEN RFC_COMERCIO = 'HDM 001017AS1' THEN 'HOME DEPOT'
WHEN RFC_COMERCIO = 'ISP 831021NV9' THEN 'INNOVA'
WHEN RFC_COMERCIO = 'MAX 0611157H8' THEN 'GNC'
WHEN RFC_COMERCIO = 'KKM 0304101S1' THEN 'KRISPY KREME'
WHEN RFC_COMERCIO = 'MKC 870629U5A' THEN 'MARY KAY'
WHEN RFC_COMERCIO = 'NME 110513PI3' THEN 'NETFLIX'
WHEN RFC_COMERCIO = 'OCI 970818KX9' THEN 'CINEMEX'
WHEN RFC_COMERCIO = 'ODM 950324V2A' THEN 'OFFICE DEPOT'
WHEN RFC_COMERCIO = 'OLO 890914R16' THEN 'LOB'
WHEN RFC_COMERCIO = 'OOM 960429832' THEN 'OFFICE MAX'
WHEN RFC_COMERCIO = 'OCI 970818KX9' THEN 'PALACIO DE HIERRO'
WHEN RFC_COMERCIO = 'P&B 0108104K7' THEN 'PULL & BEAR'
WHEN RFC_COMERCIO = 'PCO 040906RV8' THEN 'PRET COMMUNIQUE CR'
WHEN RFC_COMERCIO = 'PET 040903DH1' THEN 'PETROMAX'
WHEN RFC_COMERCIO = 'PVD 091120Q79' THEN 'PRIVALIA'
WHEN RFC_COMERCIO = 'SIH 9511279T7' THEN 'HEB'
WHEN RFC_COMERCIO = 'SSH 9608016NA' THEN 'SHASA'
WHEN RFC_COMERCIO = 'AACS970426EL6' THEN 'VOLKS KLAUSS'
WHEN RFC_COMERCIO = 'AAME490724TP7' THEN 'SAFARI TACOS CARBON'
WHEN RFC_COMERCIO = 'AAR 9411154L3' THEN 'ATLETICOS ARAGON'
WHEN RFC_COMERCIO = 'AAT 0108312VA' THEN 'AUTOSERVICIO ATLANTA'
WHEN RFC_COMERCIO = 'AAV 020404B61' THEN 'ABARROTERA AVILA'
WHEN RFC_COMERCIO = 'AAVM6811153YA' THEN 'GABRIELAS'
WHEN RFC_COMERCIO = 'ACA 990303643' THEN 'ADVANCED'
WHEN RFC_COMERCIO = 'ACO 080208S93' THEN 'ANDRE BADI'
WHEN RFC_COMERCIO = 'ADD 150727S34' THEN 'DECATHLON'
WHEN RFC_COMERCIO = 'ADF 6908013Q9' THEN 'GASOL DEL RIO'
WHEN RFC_COMERCIO = 'ADI 060418D22' THEN 'MULTIB ADICTT'
WHEN RFC_COMERCIO = 'ADM 130418IJ5' THEN 'PIRMA BRASIL'
WHEN RFC_COMERCIO = 'ADP 0102219Y9' THEN 'ARTS DENTALES PORTALES'
WHEN RFC_COMERCIO = 'ADP 0305237MA' THEN 'ART DEPORTIVOS PUEBLA'
WHEN RFC_COMERCIO = 'ADU 800131T10' THEN 'MERZA MINELLI'
WHEN RFC_COMERCIO = 'AEIA600813SQ2' THEN 'MINISUPER Y FRUTER'
WHEN RFC_COMERCIO = 'AEJR811228RE5' THEN 'ROCKSTAR BURGER'
WHEN RFC_COMERCIO = 'AEM 120605663' THEN 'AMERICAN EAGLE'
WHEN RFC_COMERCIO = 'AEN 121121HF4' THEN 'ALIANZA DE ENERGETICOS'
WHEN RFC_COMERCIO = 'AER 6201241D0' THEN 'AERS'
WHEN RFC_COMERCIO = 'AHE 040920MC8' THEN 'HAAGEN DAZS'
WHEN RFC_COMERCIO = 'AIBC560528DB1' THEN 'ESTAC CHIKRI ABIMERHI'
WHEN RFC_COMERCIO = 'AICA9110168V1' THEN 'ATTIE IZCALLI'
WHEN RFC_COMERCIO = 'AIN 911029413' THEN 'ATLETICOS INTERLOMAS'
WHEN RFC_COMERCIO = 'AIN 950517849' THEN 'SUBWAY'
WHEN RFC_COMERCIO = 'ALU 830902ST5' THEN 'LUMEN'
WHEN RFC_COMERCIO = 'AME 750808D48' THEN 'ADIDAS'
WHEN RFC_COMERCIO = 'ANE 140618P37' THEN 'AMAZON'
WHEN RFC_COMERCIO = 'ASM 131031QS4' THEN 'BLUE COLASH'
WHEN RFC_COMERCIO = 'BLI 120726UF6' THEN 'CLIP MX'
WHEN RFC_COMERCIO = 'BME 070709KF2' THEN 'BENETTON'
WHEN RFC_COMERCIO = 'CBA 951115457' THEN 'CHILIM'
WHEN RFC_COMERCIO = 'CFO 0904238R5' THEN 'CHAI'
WHEN RFC_COMERCIO = 'CFS 070215NNA' THEN 'DISH MEXICO'
WHEN RFC_COMERCIO = 'CHS 101025PG7' THEN 'HIGH STREET'
WHEN RFC_COMERCIO = 'CIA 090819PW4' THEN 'VERTICHE'
WHEN RFC_COMERCIO = 'CLK 160930GM2' THEN 'MASKOTA'
WHEN RFC_COMERCIO = 'CME 5910277L0' THEN 'CONCORD'
WHEN RFC_COMERCIO = 'CMO 161107251' THEN 'CLOE MODA'
WHEN RFC_COMERCIO = 'IUS 890616RH6' THEN 'IUSACEL'
WHEN RFC_COMERCIO = 'MOS 150123565' THEN 'PROMODA'
WHEN RFC_COMERCIO = 'NUT 840801733' THEN 'NUTRISA'
WHEN RFC_COMERCIO = 'OCO 0107276E1' THEN 'PASTELERIA OK'
WHEN RFC_COMERCIO = 'ODE 8604257UA' THEN 'DEVLYN'
WHEN RFC_COMERCIO = 'ODU 020213UDA' THEN 'EL GIRASOL'
WHEN RFC_COMERCIO = 'OFA 9009263AA' THEN 'MEN S FACTORY'
WHEN RFC_COMERCIO = 'OFU 910626UQ0' THEN 'ALSUPER'
WHEN RFC_COMERCIO = 'OME 0107208X5' THEN 'OYSHO'
WHEN RFC_COMERCIO = 'OPE 130906HN4' THEN 'OPENPAY'
WHEN RFC_COMERCIO = 'OSA 910830P43' THEN 'STOP'
WHEN RFC_COMERCIO = 'OVI 800131GQ6' THEN 'VIPS'
WHEN RFC_COMERCIO = 'PEF 950111V37' THEN 'FRAICHE'
WHEN RFC_COMERCIO = 'PMS 010531UG0' THEN 'PUMA'
WHEN RFC_COMERCIO = 'RME 120120GI7' THEN 'MR SUSHI'
WHEN RFC_COMERCIO = 'RTO 840921RE4' THEN 'TOKS'
WHEN RFC_COMERCIO = 'SDT 031013132' THEN 'SALUD DIGNA'
WHEN RFC_COMERCIO = 'SHM 1012089Z2' THEN 'SUNGLASS'
WHEN RFC_COMERCIO = 'SIS 780421IR3' THEN 'SIAPA'
WHEN RFC_COMERCIO = 'SJE 801124F40' THEN 'SEXI JEANS'
WHEN RFC_COMERCIO = 'SKI 020328NK5' THEN 'KIOSCO'
WHEN RFC_COMERCIO = 'SME 010913TS3' THEN 'SALLY BEAUTY'
WHEN RFC_COMERCIO = 'SME 110304M96' THEN 'SEPHORA'
WHEN RFC_COMERCIO = 'SME 111206QU5' THEN 'STRADIVARIUS'
WHEN RFC_COMERCIO = 'STA 9903032E9' THEN 'CARLS JR'
WHEN RFC_COMERCIO = 'STE 010604GK5' THEN 'CABLEVISION'
WHEN RFC_COMERCIO = 'SUK 931216N38' THEN 'SUKARNE'
WHEN RFC_COMERCIO = 'TAL 041210PN1' THEN 'TIENDAS OPTIMA'
WHEN RFC_COMERCIO = 'TCU 950113CS8' THEN 'CUADRA'
WHEN RFC_COMERCIO = 'TDA 8102254Q4' THEN 'TDA ARTELI'
WHEN RFC_COMERCIO = 'TEX 9302097F3' THEN 'EXTRA'
WHEN RFC_COMERCIO = 'THE 720508477' THEN 'THERMOGAS'
WHEN RFC_COMERCIO = 'TLU 080610C81' THEN 'ETN'
WHEN RFC_COMERCIO = 'TMO 991222HZ4' THEN 'LA SURTIDORA'
WHEN RFC_COMERCIO = 'TOC 930318BQ2' THEN 'TELESTAR'
WHEN RFC_COMERCIO = 'TPA 131111PM4' THEN 'EL GLOBO'
WHEN RFC_COMERCIO = 'TPT 890516JP5' THEN 'TOTAL PLAY'
WHEN RFC_COMERCIO = 'TTI 961202IM1' THEN 'TONY'
WHEN RFC_COMERCIO = 'UAM 130508KA6' THEN 'UNDERARMOUR'
WHEN RFC_COMERCIO = 'VBC 910617SR1' THEN 'TICKETMASTER MEXICO'
WHEN RFC_COMERCIO = 'VER 920215PW7' THEN 'MCDONALDS'
WHEN RFC_COMERCIO = 'VFO 830225K66' THEN 'VICKY FORM'
WHEN RFC_COMERCIO = 'VME 9608137L3' THEN 'DOROTHY GAYNOR'
WHEN RFC_COMERCIO = 'VMI 050120AU6' THEN 'ALDO CONTI'
WHEN RFC_COMERCIO = 'VMO 970612KC1' THEN 'QUARRY'
WHEN RFC_COMERCIO = 'VTH 981105F90' THEN 'VIANNEY'
WHEN RFC_COMERCIO = 'WGR 920403GN2' THEN 'CKLASS COLECCION'
WHEN RFC_COMERCIO = 'ZMC 960801538' THEN 'ZARA'
WHEN RFC_COMERCIO = 'GCD 170101GS6' THEN 'TIENDAS DEL SOL'
WHEN RFC_COMERCIO = 'CME 961203360' THEN 'C&A'
WHEN RFC_COMERCIO = 'SEM 980701STA' THEN 'SEVEN'
WHEN RFC_COMERCIO = 'TCH 850701RM1' THEN 'CHEDRAUI'
WHEN RFC_COMERCIO = 'GGU 060301LX4' THEN 'GUESS'
WHEN RFC_COMERCIO = 'SMM 0909113M6' THEN 'MILANO'
WHEN RFC_COMERCIO = 'OSM 140901RL6' THEN 'OLD NAVY'
WHEN RFC_COMERCIO = 'IBB 7712286Q8' THEN 'OSHKOSH & CARTER'
WHEN RFC_COMERCIO = 'DMP 0206057N9' THEN 'PARAZOY'
WHEN RFC_COMERCIO = 'MJS 0609252B4' THEN 'SFERA'
WHEN RFC_COMERCIO = 'MME 081121EI2' THEN 'STUDIO F'
WHEN RFC_COMERCIO = 'WDM 990126350' THEN 'WALDOS'
WHEN RFC_COMERCIO = 'THE 950510BL9' THEN 'FIORENTINA'
WHEN RFC_COMERCIO = 'TAD 140205H99' THEN 'ADITIVO'
WHEN RFC_COMERCIO = 'GAN 891024M25' THEN 'OGGI JEANS'
WHEN RFC_COMERCIO = 'SIN 830418RK2' THEN 'SANTORY'
WHEN RFC_COMERCIO =	'ROM 901219IC9' THEN 'LIZ MINELLI'
WHEN RFC_COMERCIO = 'RST 141127478' THEN 'VICTORIA S SECRET'
WHEN RFC_COMERCIO = 'COC 911115J81' THEN 'TROPIC'
WHEN RFC_COMERCIO = 'BAS 0108275N9' THEN 'CK - TOMMY'
WHEN RFC_COMERCIO = 'MDM 041221RJ3' THEN 'MASSIMO DUTTI'
WHEN RFC_COMERCIO = 'BMO 1508149R3' THEN 'NINA FERRE'
WHEN RFC_COMERCIO =	'IDS 151021E44' THEN 'QUARRY JEANS'
WHEN RFC_COMERCIO = 'SMO 160215A23' THEN 'SOHO MEXICO'
WHEN RFC_COMERCIO = 'GSE 900914A29' THEN 'SR FROGS'
WHEN RFC_COMERCIO = 'JAX 840731BL9' THEN 'BOUTIQUE LINEAS'
WHEN RFC_COMERCIO = 'OAC 1112068G6' OR RFC_COMERCIO = 'OEX 9602014B9' THEN 'BURGER KING'
WHEN (NOMBRE_COMERCIO LIKE'UBER%' OR NOMBRE_COMERCIO LIKE'% UBER%' OR NOMBRE_COMERCIO LIKE'%*UBER%' OR NOMBRE_COMERCIO LIKE'%UBER*%') AND NOMBRE_COMERCIO NOT LIKE'%EATS%' THEN 'UBER'
WHEN NOMBRE_COMERCIO LIKE '%DIDI%' AND NOMBRE_COMERCIO NOT LIKE '%DIDI%FOOD%' AND NOMBRE_COMERCIO NOT LIKE '%DIDIHER%' THEN 'DIDI'
WHEN RFC_COMERCIO = 'VPS 100716CK9' AND NOMBRE_COMERCIO LIKE '%TELCEL%' THEN 'TELCEL' 
WHEN RFC_COMERCIO = 'VPS 100716CK9' AND NOMBRE_COMERCIO LIKE '%MOVISTAR%' THEN 'MOVISTAR' 
WHEN RFC_COMERCIO IN ('CME 981208VE4','TCI 121023F10') THEN 'CINEPOLIS'
WHEN RFC_COMERCIO = 'TSO 991022PB6' AND NOMBRE_COMERCIO NOT LIKE 'CITY%' THEN 'SORIANA'
WHEN RFC_COMERCIO = 'TSO 991022PB6' AND NOMBRE_COMERCIO LIKE 'CITY%' THEN 'CITY CLUB'		  
WHEN RFC_COMERCIO = 'OPM 150323DI1' OR NOMBRE_COMERCIO LIKE 'PAYPAL%' AND RFC_COMERCIO NOT IN ('OPM 150323DI1') THEN 'PAYPAL'
WHEN RFC_COMERCIO  IN ('GVA 010601FT9','KUDR7112168K5') THEN 'VANITY'
WHEN NOMBRE_COMERCIO LIKE '%DIDI%FOOD%' OR RFC_COMERCIO = 'DMM 171208LT4' THEN 'DIDI FOOD'
WHEN RFC_COMERCIO = 'TEC 140101HZ9' OR RFC_COMERCIO = 'HAC 861114P16' THEN 'GRUPO CALIENTE'
WHEN RFC_COMERCIO = 'TRA 150604TW1' OR RFC_COMERCIO = 'SPM 1410037E8' THEN 'RAPPI'
WHEN RFC_COMERCIO = 'PRE 100204N30' OR RFC_COMERCIO = 'PRE 100204N30' THEN 'PRICE TRAVEL'
WHEN RFC_COMERCIO = 'AME 900126RZ5' OR RFC_COMERCIO = 'AME 900126RZ5' THEN 'AMWAY'
WHEN NOMBRE_COMERCIO LIKE 'SUBURBIA%TOL%' OR RFC_COMERCIO = 'SUB 910603SB3' OR RFC_COMERCIO = 'AUR 9402236Y6' THEN 'SUBURBIA'
WHEN RFC_COMERCIO = 'CCM 010816UK4' OR RFC_COMERCIO = 'CAB 6610044K1' THEN 'IZZI'
WHEN RFC_COMERCIO = 'DLI 931201M19' OR RFC_COMERCIO = 'DLI 931201MI9' THEN 'LIVERPOOL'
WHEN RFC_COMERCIO = 'ECE 9610253TA' OR RFC_COMERCIO = 'EMI 790601FN5' THEN 'ELEKTRA'
WHEN RFC_COMERCIO = 'OCJ 980219MI5' OR RFC_COMERCIO = 'OCJ 980219M15' OR RFC_COMERCIO = 'ORE 980722BZ1' THEN 'SMART'
WHEN RFC_COMERCIO = 'RDI 841003QJ4'OR  RFC_COMERCIO = 'RDI 841003Q54' THEN 'TELCEL'
WHEN RFC_COMERCIO = 'ACM 090729KD0'	OR RFC_COMERCIO = 'ACS 100407M72' THEN 'ACCCOMM'
WHEN RFC_COMERCIO = 'CIN 970804515' OR RFC_COMERCIO = 'CMU 8312025B5' OR RFC_COMERCIO = 'CAL 910621LJ3' OR RFC_COMERCIO = 'CCA 100430156' THEN 'ZAP'
WHEN RFC_COMERCIO = 'API 090422UG3' OR RFC_COMERCIO = 'CCA 1308213W7' OR RFC_COMERCIO = 'PCA 0810272Y0' THEN 'LITTLE CAESARS'
WHEN RFC_COMERCIO = 'CNM 980114PI2' OR RFC_COMERCIO = 'CNM 980114P12' THEN 'AT&T'
WHEN RFC_COMERCIO = 'ODO 910311U70' OR RFC_COMERCIO = 'OPP 010927SA5' OR RFC_COMERCIO = 'OAP 1411219D4' THEN 'DOMINOS'
WHEN RFC_COMERCIO = 'ARO 860923TK0' OR RFC_COMERCIO = 'OFS 170830SB1' OR RFC_COMERCIO = 'RAD 161031RK1' OR RFC_COMERCIO = 'VAL 901115TZ8' THEN 'MCDONADLS'
WHEN RFC_COMERCIO = 'CCF 121101KQ4' OR  RFC_COMERCIO = 'TCM 951030A17' THEN 'COMERCIAL MEXICANA'
WHEN RFC_COMERCIO = 'BME 071214DM3' OR RFC_COMERCIO = 'BST 1911113V0' THEN 'BOBOIS'
WHEN ((RFC_COMERCIO = 'MER 991006JMA' AND POS_ENTRY_MODE IN ('01','10')) OR (RFC_COMERCIO = 'MAG 2105031W3' AND POS_ENTRY_MODE IN ('01','10'))) THEN 'MERCADO LIBRE ONLINE'
WHEN ((RFC_COMERCIO = 'MER 991006JMA' AND POS_ENTRY_MODE IN ('05','07','90')) OR (RFC_COMERCIO = 'MAG 2105031W3' AND POS_ENTRY_MODE IN ('05','07','90'))) THEN 'MERCADO LIBRE OFFLINE'
WHEN RFC_COMERCIO = 'NWM 9709244W4' AND (NOMBRE_COMERCIO LIKE 'B%' OR NOMBRE_COMERCIO LIKE 'MI%')THEN 'BODEGA'	
WHEN RFC_COMERCIO = 'NWM 9709244W4' AND ([CLAVE_COMERCIO] LIKE '%4163436' OR CLAVE_COMERCIO LIKE '%4163435' OR CLAVE_COMERCIO LIKE '%4302584' OR CLAVE_COMERCIO LIKE '%8435228' OR CLAVE_COMERCIO LIKE '%8435228' OR CLAVE_COMERCIO LIKE '%4392592' OR CLAVE_COMERCIO LIKE '%4194989' OR CLAVE_COMERCIO LIKE '%4044712' OR CLAVE_COMERCIO LIKE '%4180118' OR CLAVE_COMERCIO LIKE  '%8434689' OR CLAVE_COMERCIO LIKE '%4302592') THEN 'BODEGA'
WHEN (RFC_COMERCIO = 'NWM 9709244W4' AND (NOMBRE_COMERCIO LIKE '%SAM%' OR NOMBRE_COMERCIO LIKE '% REN%') AND (NOMBRE_COMERCIO NOT LIKE '%WAL%' OR NOMBRE_COMERCIO NOT LIKE 'BAE%')) THEN 'SAMS'
WHEN (RFC_COMERCIO = 'NWM 9709244W4' AND (NOMBRE_COMERCIO LIKE '%SUPERAMA%' OR NOMBRE_COMERCIO LIKE '%SUPREMA%')) THEN 'WALMART EXPRESS'
WHEN (RFC_COMERCIO = 'NWM 9709244W4' AND RIGHT(CLAVE_COMERCIO,7) IN ('4180706','4180705','4315440','4194988')) THEN 'WALMART ONLINE'
WHEN (RFC_COMERCIO = 'NWM 9709244W4' AND (NOMBRE_COMERCIO LIKE '%WAL%' OR NOMBRE_COMERCIO LIKE '%TDAS%' OR NOMBRE_COMERCIO LIKE 'SUPCENT%' OR NOMBRE_COMERCIO LIKE '%SUPER%')) AND RIGHT(CLAVE_COMERCIO,7) NOT IN ('4180706','4180705','4315440','4194988') THEN 'WALMART OFFLINE'	

            ELSE NOMBRE_COMERCIO  -- Si no hay una coincidencia, mantener el nombre original
        END AS MAPPED_NOMBRE_COMERCIO
    FROM PROSA_510
    WHERE FECHA_CONSUMO >= '2022-01-01 00:00:00.000' AND 
          FECHA_CONSUMO <= '2023-09-13 00:00:00.000' AND 
          TIPO_TRANSACCION = '01'
)

SELECT  
    cm.RFC_COMERCIO,
    FECHA_CONSUMO,
    COUNT(DISTINCT NUM_CUENTA) AS NUM_CUENTAS_UNICAS,
    COUNT(IMP_DESTINO) AS TXN,
    SUM(IMP_DESTINO) AS MONTO_IMP_DESTINO_POR_DIA,
    CASE
        WHEN cm.MAPPED_NOMBRE_COMERCIO IS NOT NULL THEN cm.MAPPED_NOMBRE_COMERCIO
        ELSE 'OTHER'
    END AS MAPPED_NOMBRE_COMERCIO
FROM PROSA_510
LEFT JOIN comercio_mapping cm ON PROSA_510.RFC_COMERCIO = cm.RFC_COMERCIO
WHERE FECHA_CONSUMO >= '2022-01-01 00:00:00.000' AND 
      FECHA_CONSUMO <= '2023-09-13 00:00:00.000' AND 
      TIPO_TRANSACCION = '01'
GROUP BY FECHA_CONSUMO, cm.RFC_COMERCIO, cm.MAPPED_NOMBRE_COMERCIO
ORDER BY FECHA_CONSUMO, cm.RFC_COMERCIO;