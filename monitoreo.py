"""En está área se establece la comunicación desde la intranet hacia la pasarela 
para enviar la información obtenida por RestMonitoring, cada cierto período de tiempo, 
con el fin de almacenarla en la base de datos. La información recopilada por RestMonitoring
en cuanto al sistema operativo es : nombre del kernel, release del kernel, nombre del nodo, 
versión del kernel, máquina, procesador, sistema operativo y hardware, en cuanto al usuario es: 
usuario activo, en cuanto a un usuario en particular es: si está activo o no, en cuanto al uso 
de la CPU es: tiempo dedicado a ejecutar código que no es del kernel, tiempo dedicado a ejecutar 
el código del  kernel, tiempo de inactividad, tiempo dedicado a esperar un dispositivo de E/S  
y tiempo robado por una máquina virtual, en cuanto al uso de la memoria es: cantidad de memoria virtual 
utilizada, cantidad de memoria disponible, cantidad de memoria utilizada como buffer y cantidad de memoria 
utilizada como caché, y en cuanto a memoria de intercambio es: cantidad de memoria de intercambio desde el 
disco y cantidad de memoria de intercambio en el disco. Teniendo en cuenta que esta información es recibida 
de RestMonitoring en formato JSON."""   

