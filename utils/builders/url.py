# -*- coding: utf-8 -*-
class URLBuilder:
	@staticmethod
	def build(origem, destino, dataida, datavolta, quantidadeadultos, quantidadecriancas, somenteida = "false"):
		return "http://www.submarinoviagens.com.br/Passagens/selecionarvoo?SomenteIda=%s&Origem=--%s---&Destino=--%s---&Origem=--%s---&Destino=--%s---&Data=%s&Data=%s&NumADT=%s&NumCHD=%s&NumINF=0&SomenteDireto=&Hora=&Hora=&selCabin=&Multi=false" % (somenteida, origem, destino, destino, origem, dataida, datavolta, quantidadeadultos, quantidadecriancas)