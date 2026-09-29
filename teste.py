import requests

from pprint import pprint # BIBLIOTECA PARA IMPRIMIR OS DADOS DE FORMA LEGÍVEL

api_key = "9960edfc48c345248e3230552262909"
api_link = "http://api.weatherapi.com/v1"

parametros = {
"key": api_key,
"q": "São Paulo", # CIDADE PARA QUAL QUEREMOS OBTER OS DADOS
"lang": "pt" # LINGUAGEM
}
# ARMAZENANDO A RESPOSTA DA REQUISIÇÃO NA VARIÁVEL RESPOSTA

resposta = requests.get(api_link, params=parametros)