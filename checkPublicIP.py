#!/usr/bin/python
# -*- coding: utf-8 -*-

#######################################################
##                                                   ##
## Script principal para comprobar si la IP pública  ##
## ha cambiado e informar por e-mail de dicho cambio ##
##                                                   ##
##                  www.manusoft.es                  ##
##                                                   ##
#######################################################


# Importamos el módulo necesario para obtener la dirección IP pública
from getPublicIP import getPublicIP
# Importamos el módulo necesario para comprobar si la dirección IP pública ha cambiado
from checkActualIP import checkActualIP
# Importamos el módulo necesario para enviar correos electrónicos
from sendMail import sendMail

# << Inicio de la definición

def checkPublicIP(src, pwd, dst):
	# Comprobamos si la dirección IP pública ha cambiado
	if (not checkActualIP()):
		# Si la IP actual no coincide con la registrada, enviamos la nueva IP por correo electrónico
		sendMail(src, pwd, dst, "Nueva IP", getPublicIP())

# >> Fin de la definición

####################
## FIN DEL SCRIPT ##
####################
