import requests

from pprint import pprint # BIBLIOTECA PARA IMPRIMIR OS DADOS DE FORMA LEGÍVEL

api_key = "9960edfc48c345248e3230552262909"
api_link = "http://api.weatherapi.com/v1/current.json"

parametros = {
"key": api_key,
"q": "París", # CIDADE PARA QUAL QUEREMOS OBTER OS DADOS
"lang": "fr",   # LINGUAGEM
}
# ARMAZENANDO A RESPOSTA DA REQUISIÇÃO NA VARIÁVEL RESPOSTA

resposta = requests.get(api_link, params=parametros)

#print(resposta.status_code)

#print(resposta.content)

cidade = parametros["q"]

if resposta.status_code == 200:
    print("Requisição realizada com Sucesso!")
    dados = resposta.json() # ARMAZENANDO OS DADOS EM FORMATO JSON NA VARIÁVEL DADOS
    #pprint(dados)#.json()bonitinho
    temperatura = dados["current"]["temp_c"] # ARMAZENANDO A TEMPERATURA EM °C
    descricao = dados["current"]["condition"]["text"] # ARMAZENANDO DESCRIÇÃO
    print(f"A temperatura atual em {cidade} é de: {temperatura} °C")
    print(f"Descrição do Clima: {descricao}")
else: 
    print("Erro na requisição")