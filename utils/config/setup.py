# -*- coding: utf-8 -*-
import os
import ConfigParser
 
class Configuration:
	
	def load(self):
		config = ConfigParser.ConfigParser()
		 
		# Lê o seu arquivo com as definições de seções e itens.
		config.read(os.path.abspath(os.path.dirname(__file__)) + '/../../config/config.cfg')
		self.__config = {i[0]: i[1] for i in config.items('configurations')}

	def getProperty(self, name):
		return self.__config.get(name)