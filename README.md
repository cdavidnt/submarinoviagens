# SOBRE #

Programa de pesquisa de passagens no site http://www.submarinoviagens.com.br/
Ao ser executado, o programa faz uma busca a cada 10 minutos no site para busca de passagens e envia um e-mail caso o preço da passagem tenha mudado


# REQUERIMENTOS #

Python 2.7  
pip  

## SETUP ##

pip install -r requirements


## CONFIGURACAO ##

Preencher as propriedades no arquivo config/config.cfg  

email = [seu e-mail no GMAIL]  
password = [senha do seu GMAIL]  

origem = [CODIGO DO AEROPORTO DE ACORDO COM A LISTA http://pt.wikipedia.org/wiki/Anexo:Lista_de_aeroportos_do_Brasil]  
destino = [CODIGO DO AEROPORTO DE ACORDO COM A LISTA http://pt.wikipedia.org/wiki/Anexo:Lista_de_aeroportos_do_Brasil]  

datadeida = dd/mm/aaaa  
datadevolta = dd/mm/aaaa  

quantidadeadultos = 1  
quantidadecriancas = 0  

## RODANDO O PROGRAMA ##

python verifica.py
