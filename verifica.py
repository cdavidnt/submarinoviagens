# -*- coding: utf-8 -*-

import time
import sys, traceback
from utils.config.setup import Configuration
from utils.builders.url import URLBuilder

from selenium import webdriver
from notifier import Notifier

config = Configuration()
config.load()
origem = config.getProperty("origem")
destino = config.getProperty("destino")
dataida = config.getProperty("datadeida")
datavolta = config.getProperty("datadevolta")
somenteida = config.getProperty("somenteida")
quantidadeadultos = config.getProperty("quantidadeadultos")
quantidadecriancas = config.getProperty("quantidadecriancas")

email = Notifier(config.getProperty("email"),config.getProperty("password"))


driver = webdriver.Firefox()
driver.get(URLBuilder.build(origem, destino, dataida, datavolta, quantidadeadultos, quantidadecriancas, somenteida))

contador = 0

while 1:
	subject = "[PASSAGENS SUBMARINOVIAGENS]"
	try:

		while driver.find_element_by_id("btnBestPriceNoStop").text == '':
			contador += 1
			time.sleep(5)
			if contador > 10:
				raise Exception('Maximo de tentativas excedidas para tentar o preço')


		valor = driver.find_element_by_id("btnBestPriceNoStop").text
		ultimo_valor = ''
		try:
			ultimo_valor = open('ultimo_valor', 'r').readline()
		except IOError:
			print "Nao existe valor anterior"
		f = open('ultimo_valor', 'w')
		f.write(valor)

		if ultimo_valor is None  or ultimo_valor != valor:
			conteudo = driver.find_element_by_id("divMatrixPrice").text
			subject = "%s %s" % (subject, valor)
			email.deliver(subject,conteudo)

	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
		email.deliver(subject + "HOUVE UM ERRO AO PROCESSAR SEU PREÇO")
	driver.quit()
	time.sleep(600)