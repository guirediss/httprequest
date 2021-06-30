import requests
import json

resposta = requests.get('https://api.github.com/users/guirediss')

if(resposta.status_code == 200):
    dados = resposta.json()
    print(dados['name'])
    print(dados['location'])
    print(dados['company'])
else:
    print(resposta.status_code)




