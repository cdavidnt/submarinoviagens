# REQUERIMENTOS #

Python 2.7
pip

## SETUP ##

pip install -r requirements


## CONFIGURACAO ##

Preencher as propriedades no arquivo config/config.cfg

Para a propriedade 'url', fazer primeiramente uma pesquisa no submarinoviagens.com.br e copiar a url final de pesquisa de precos
url = [URL DE ACESSO À PAGINA DE PESQUISA DE PRECOS DO SUBMARINO]
ex: 
url = http://www.submarinoviagens.com.br/Passagens/selecionarvoo?SomenteIda=false&Origem=Recife%20/%20PE,%20Brasil,%20Guararapes%20--REC---&Destino=Sao%20Paulo%20/%20SP,%20Brasil,%20Congonhas%20--CGH---&Origem=Sao%20Paulo%20/%20SP,%20Brasil,%20Congonhas%20--CGH---&Destino=Recife%20/%20PE,%20Brasil,%20Guararapes%20--REC---&Data=26/07/2013&Data=30/07/2013&NumADT=1&NumCHD=0&NumINF=0&SomenteDireto=&Hora=&Hora=&selCabin=&Multi=false

email = [seu e-mail no GMAIL]
password = [senha do seu GMAIL]

## RODANDO O PROGRAMA ##

python verifica.py