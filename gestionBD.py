""" Este módulo se encarga de establecer la conexión con la base de datos 
para crear un nuevo registro, modificar uno ya existente o consultarlo.

En esta base de datos existirán las siguientes entidades con los siguientes
atributos:

sistemaOpertativo: (kernel, release, nodo, version, maquina, procesador, so, hardware)

usuario: (nombre)

cpu: (noKernel, kernel, inactividad, esperaES, maquinaVirtual)

memoria: (virtual, disponible, buffer, cache)

memoriaIntercambio: (desdeDisco, enElDisco)

descargas: (link)

"""
