#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################
##                                            ##
## Script para comprobar la IP pública actual ##
## con la IP pública almacenada de un fichero ##
##                                            ##
##               www.manusoft.es              ##
##                                            ##
################################################



# Importamos la librería necesaria para acceder a un fichero
import os.path as path
# Importamos el módulo encargado de obtener la dirección IP pública actual
from getPublicIP import getPublicIP

def checkActualIP():
	# Apertura del fichero con la última dirección IP pública registrada
	# Comprobamos que el ficheor existe
	if path.exists('publicIPs.txt'):
		# Si el fichero existe, lo abrimos en modo lectura. El atributo 'r' indica que es de solo lectura
		archivo = open("publicIPs.txt", 'r')
	else:
		# Si el archivo no existe, lo creamos en modo lectura y escritura. El atributo 'w+' abre el fichero en modo lectura y escritura y, si no existe, lo crea
		archivo = open("publicIPs.txt", 'w+')
	# Obtenemos la dirección IP pública actual.
	publicIpActual = getPublicIP().split('\n')[0]

	# << Lectura de la última dirección IP pública registrada en el fichero
	# Se leen todas las líneas del fichero, quedándonos únicamente con la última
	linea = archivo.readline()
	publicIParchivada = ""
	while linea != '':
		publicIParchivada = linea
		linea = archivo.readline()

	archivo.close()
	return publicIParchivada, publicIpActual
####################
## FIN DEL SCRIPT ##
####################
