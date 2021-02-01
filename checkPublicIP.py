#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Importamos el módulo necesario para obtener la dirección IP pública
from getPublicIP import getPublicIP
# Importamos el módulo necesario para comprobar si la dirección IP pública ha cambiado
from checkActualIP import checkActualIP
# Importamos el módulo necesario para enviar correos electrónicos
from sendMail import sendMail
# Importamos el módulo necesario para recibir los parámetros desde consola
import sys
from datetime import datetime
# << Inicio de la definición

def checkPublicIP(src, pwd, dst):
	# Comprobamos si la dirección IP pública ha cambiado
	now = datetime.now()
	publicIParchivada, publicActualIP = checkActualIP()
	if publicIParchivada == "" or publicIParchivada != publicActualIP:
             # Guardamos la dirección IP pública actual en la variable "publicIP"
                # Escribimos la dirección IP pública actual en el fichero "publicIPs.txt". El atrib$
		archivo = open("publicIPs.txt", 'w+')
		archivo.write(publicActualIP)
		# Cerramos el fichero
		archivo.close()
		sub="Ha cambiado la IP Publica de casa"
		msg ="La nueva IP Public de casa es:  " + publicActualIP + " a las:  " + str(now)
		# Si la IP actual no coincide con la registrada, enviamos la nueva IP por correo el$
		sendMail(src, pwd, dst, sub, msg)

#Esta parte se oculta por que ahora se ejecuta el script cada 10 minutos y no veo necesario recibir un mail cada 10 minutos,
#ya se ha comprobado que funciona, mas adelante veremos si esta parte del codigo desaparece por completo
#	else:
#		sub="Estado de la Ip Publica de Casa"
#		msg ="La Ip de Casa sigue siendo " + publicIParchivada  + " la misma a las " + str(now)
                # Si la Ip es la misma que tenia guardada, no hay problema
                #sendMail(src, pwd, dst, sub, msg)
#	sendMail(src, pwd, dst, sub, msg)
# >> Fin de la definición

# << Inicio de la invocación
checkPublicIP(sys.argv[1],sys.argv[2],sys.argv[3])
# >> Fin de la invocación

####################
## FIN DEL SCRIPT ##
####################
