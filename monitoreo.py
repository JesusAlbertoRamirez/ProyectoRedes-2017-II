"""En est� �rea se establece la comunicaci�n desde la intranet hacia la pasarela 
para enviar la informaci�n obtenida por RestMonitoring, cada cierto per�odo de tiempo, 
con el fin de almacenarla en la base de datos. La informaci�n recopilada por RestMonitoring
en cuanto al sistema operativo es : nombre del kernel, release del kernel, nombre del nodo, 
versi�n del kernel, m�quina, procesador, sistema operativo y hardware, en cuanto al usuario es: 
usuario activo, en cuanto a un usuario en particular es: si est� activo o no, en cuanto al uso 
de la CPU es: tiempo dedicado a ejecutar c�digo que no es del kernel, tiempo dedicado a ejecutar 
el c�digo del  kernel, tiempo de inactividad, tiempo dedicado a esperar un dispositivo de E/S  
y tiempo robado por una m�quina virtual, en cuanto al uso de la memoria es: cantidad de memoria virtual 
utilizada, cantidad de memoria disponible, cantidad de memoria utilizada como buffer y cantidad de memoria 
utilizada como cach�, y en cuanto a memoria de intercambio es: cantidad de memoria de intercambio desde el 
disco y cantidad de memoria de intercambio en el disco. Teniendo en cuenta que esta informaci�n es recibida 
de RestMonitoring en formato JSON."""   

