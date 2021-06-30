import requests
import json

resposta = requests.get('https://api.github.com/users/guirediss')

print(resposta.status_code)
dados = resposta.json()
print(dados['name'])
print(dados['location'])
print(dados['company'])




