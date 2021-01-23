#!/usr/bin/python
# -*- coding: utf-8 -*-



# Importamos la librería necesaria para el envío de correos
from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib


def sendMail(src, pwd, dst, sub, mensage):
	# << Montaje del correo electrónico
	msg = MIMEMultipart()
	msg['From'] =src
	msg['To'] = dst
	msg['Subject'] = sub
	msg.attach(MIMEText(mensage, 'plain'))
	# >> Fin del montaje del correo electrónico
	# << Envío del correo
	# Apertura del servido SMTP en el servidor de correo electrónico de origen
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		try:
			# Inicio de sesión en el servidor de correo electrónico de origen.
			server.login(msg['From'], pwd)
			try:
				# Envío del correo electrónico
				server.sendmail(msg['From'], msg['To'], msg.as_string())
			except:
				print('Error al enviar el correo electrónico')
		except:
			print('Error al iniciar sesión en GMail')
		# Cierre del servidor SMTP
		server.quit()
	except:
		print('Error al iniciar el servidor SMTP')
	# >> Fin del envío del correo



# Fin del Script

