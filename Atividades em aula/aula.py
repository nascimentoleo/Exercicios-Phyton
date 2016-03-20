def imprimeLista(lista):
    for cadaitem in lista:
    	if(isinstance(cadaitem, list)):
    		imprimeLista(cadaitem)
    	else:
    		print(cadaitem);

imprimeLista(["eles","tu", "eu", ["123", 4, "derg"]]);
