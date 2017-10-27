"""Este módulo se encarga de establecer la conexión con la base de datos 
para crear un nuevo registro, modificar uno ya existente o consultarlo, 
teniendo en cuenta que la intranet es la que puede crear y modificar registros, 
mientras que el cliente es el encargado de hacer consultas.

En esta base de datos existirán las siguientes entidades con los siguientes
atributos:

sistemaOpertativo: (kernel, release, nodo, version, maquina, procesador, so, hardware)

usuario: (nombre)

cpu: (noKernel, kernel, inactividad, esperaES, maquinaVirtual)

memoria: (virtual, disponible, buffer, cache)

memoriaIntercambio: (desdeDisco, enElDisco)

"""
