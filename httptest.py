import requests

resposta = requests.get('https://api.github.com')

#print(resposta.status_code)

#dados = resposta.text
dados = resposta.json()
print(dados['current_user_url'])



