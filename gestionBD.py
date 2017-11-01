""" Este módulo se encarga de establecer la conexión con la base de datos 
para crear un nuevo registro, modificar uno ya existente o consultarlo.

En esta base de datos existirán las siguientes entidades con los siguientes
atributos:

sistemaOpertativo: (id, kernel, release, nodo, version, maquina, procesador, so, hardware)

usuario: (id, nombre)

cpu: (id, noKernel, kernel, inactividad, esperaES, maquinaVirtual)

memoria: (id, virtual, disponible, buffer, cache)

memoriaIntercambio: (id, desdeDisco, enElDisco)

descargas: (id, link, progreso)

monitoreo: (id, peticion)

"""
